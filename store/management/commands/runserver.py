"""Runserver for this project only: use a free port, then open the browser."""

from __future__ import annotations

import os
import socket
import subprocess
import sys
import threading
import webbrowser

from django.contrib.staticfiles.management.commands.runserver import (
    Command as BaseRunserverCommand,
)

FALLBACK_PORTS = (8000, 9000, 7000, 5000, 4000)


class Command(BaseRunserverCommand):
    help = (
        'Starts a development server for the project in this folder, '
        'picks a port Windows will allow, and opens the browser.'
    )

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            '--no-browser',
            action='store_true',
            help='Do not open a browser window.',
        )

    def handle(self, *args, **options):
        self._open_browser = not options.pop('no_browser', False)
        addrport = options.get('addrport') or ''
        host, port = self._parse_addrport(addrport)

        if addrport:
            self._free_port(port)
        else:
            port = self._first_bindable_port(host, FALLBACK_PORTS)
            options['addrport'] = str(port)
            if port != int(self.default_port):
                self.stdout.write(self.style.WARNING(
                    f'Port {self.default_port} is reserved by Windows. '
                    f'Using http://127.0.0.1:{port}/'
                ))

        self._browser_host = '127.0.0.1' if host in ('0.0.0.0', '::', '') else host
        self._browser_port = port
        return super().handle(*args, **options)

    def inner_run(self, *args, **options):
        if getattr(self, '_open_browser', True):
            url = f'http://{self._browser_host}:{self._browser_port}/'
            threading.Timer(1.2, lambda: webbrowser.open(url)).start()
            self.stdout.write(self.style.SUCCESS(f'Opening {url} (this project folder)'))
        return super().inner_run(*args, **options)

    def _parse_addrport(self, addrport: str):
        default_port = int(self.default_port)
        default_addr = self.default_addr
        if not addrport:
            return default_addr, default_port
        if addrport.isdigit():
            return default_addr, int(addrport)
        if ':' in addrport:
            host, _, port = addrport.rpartition(':')
            return (host or default_addr), int(port or default_port)
        return addrport, default_port

    def _can_bind(self, host: str, port: int) -> bool:
        bind_host = '127.0.0.1' if host in ('0.0.0.0', '::', '') else host
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.bind((bind_host, port))
            return True
        except OSError:
            return False

    def _first_bindable_port(self, host: str, ports: tuple[int, ...]) -> int:
        for port in ports:
            if self._can_bind(host, port):
                return port
        return ports[0]

    def _free_port(self, port: int):
        """Stop whatever is already listening on this port (Windows)."""
        if sys.platform != 'win32':
            return
        try:
            out = subprocess.check_output(['netstat', '-ano'], text=True, errors='ignore')
        except Exception:
            return

        skip = {str(os.getpid()), str(os.getppid()), '0'}
        pids = set()
        needle = f':{port}'
        for line in out.splitlines():
            if 'LISTENING' not in line.upper() or needle not in line:
                continue
            parts = line.split()
            pid = parts[-1] if parts else ''
            if pid.isdigit() and pid not in skip:
                pids.add(pid)

        for pid in pids:
            subprocess.run(
                ['taskkill', '/F', '/PID', pid],
                capture_output=True,
                check=False,
            )
            self.stdout.write(self.style.WARNING(
                f'Freed port {port} (stopped PID {pid}) so this project can use it.'
            ))

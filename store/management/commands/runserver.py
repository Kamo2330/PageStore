"""Runserver for this project only: free the port, then open the browser."""

from __future__ import annotations

import os
import subprocess
import sys
import threading
import webbrowser

from django.contrib.staticfiles.management.commands.runserver import (
    Command as BaseRunserverCommand,
)


class Command(BaseRunserverCommand):
    help = (
        'Starts a development server for the project in this folder, '
        'frees the port if another app is using it, and opens the browser.'
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
        host, port = self._parse_addrport(options.get('addrport') or '')
        self._free_port(port)
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

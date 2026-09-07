"""Demo catalog for PageStore — static product data for the storefront demo."""

PRODUCTS = [
    {
        "id": "ps-001",
        "name": "Harare Linen Shirt",
        "price": 529,
        "compare_at": None,
        "category": "tops",
        "gender": "men",
        "color": "white",
        "sizes": ["S", "M", "L", "XL"],
        "badge": "New",
        "image": "https://images.unsplash.com/photo-1596755094514-f87e34085bdc?q=80&w=1200&auto=format&fit=crop",
        "blurb": "Breathable linen, cut for warm days.",
    },
    {
        "id": "ps-002",
        "name": "Cape Town Wide Trouser",
        "price": 689,
        "compare_at": None,
        "category": "bottoms",
        "gender": "women",
        "color": "black",
        "sizes": ["S", "M", "L"],
        "badge": "New",
        "image": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?q=80&w=1200&auto=format&fit=crop",
        "blurb": "Relaxed fit with a sharp crease.",
    },
    {
        "id": "ps-003",
        "name": "Soweto Essential Tee",
        "price": 349,
        "compare_at": None,
        "category": "tops",
        "gender": "men",
        "color": "black",
        "sizes": ["S", "M", "L", "XL"],
        "badge": None,
        "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?q=80&w=1200&auto=format&fit=crop",
        "blurb": "Soft cotton, everyday staple.",
    },
    {
        "id": "ps-004",
        "name": "Lagos Knit Dress",
        "price": 799,
        "compare_at": 999,
        "category": "tops",
        "gender": "women",
        "color": "teal",
        "sizes": ["S", "M", "L"],
        "badge": "Sale",
        "image": "https://images.unsplash.com/photo-1595777457583-95e059d581b8?q=80&w=1200&auto=format&fit=crop",
        "blurb": "Fluid knit that moves with you.",
    },
    {
        "id": "ps-005",
        "name": "Durban Canvas Tote",
        "price": 279,
        "compare_at": None,
        "category": "accessories",
        "gender": "accessories",
        "color": "teal",
        "sizes": ["One size"],
        "badge": None,
        "image": "https://images.unsplash.com/photo-1590874103328-eac38a67478a?q=80&w=1200&auto=format&fit=crop",
        "blurb": "Sturdy canvas for market days.",
    },
    {
        "id": "ps-006",
        "name": "Joburg Classic Hoodie",
        "price": 649,
        "compare_at": 899,
        "category": "tops",
        "gender": "men",
        "color": "black",
        "sizes": ["S", "M", "L", "XL"],
        "badge": "Sale",
        "image": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?q=80&w=1200&auto=format&fit=crop",
        "blurb": "Heavyweight fleece, city-ready.",
    },
    {
        "id": "ps-007",
        "name": "Accra Pleated Skirt",
        "price": 559,
        "compare_at": None,
        "category": "bottoms",
        "gender": "women",
        "color": "white",
        "sizes": ["S", "M", "L"],
        "badge": "New",
        "image": "https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?q=80&w=1200&auto=format&fit=crop",
        "blurb": "Light pleats, easy elegance.",
    },
    {
        "id": "ps-008",
        "name": "Nairobi Kids Tee",
        "price": 229,
        "compare_at": None,
        "category": "tops",
        "gender": "kids",
        "color": "white",
        "sizes": ["4", "6", "8", "10"],
        "badge": None,
        "image": "https://images.unsplash.com/photo-1519238263530-99bdd11df2ea?q=80&w=1200&auto=format&fit=crop",
        "blurb": "Soft jersey built for play.",
    },
    {
        "id": "ps-009",
        "name": "Kigali Crossbody Bag",
        "price": 449,
        "compare_at": 549,
        "category": "accessories",
        "gender": "accessories",
        "color": "black",
        "sizes": ["One size"],
        "badge": "Sale",
        "image": "https://images.unsplash.com/photo-1548036328-c9fa89d128ac?q=80&w=1200&auto=format&fit=crop",
        "blurb": "Compact leather, hands-free.",
    },
    {
        "id": "ps-010",
        "name": "Maputo Denim Jacket",
        "price": 899,
        "compare_at": None,
        "category": "tops",
        "gender": "women",
        "color": "teal",
        "sizes": ["S", "M", "L"],
        "badge": None,
        "image": "https://images.unsplash.com/photo-1551028719-00167b16eac5?q=80&w=1200&auto=format&fit=crop",
        "blurb": "Washed denim with a soft hand.",
    },
    {
        "id": "ps-011",
        "name": "Pretoria Chino Short",
        "price": 399,
        "compare_at": None,
        "category": "bottoms",
        "gender": "men",
        "color": "white",
        "sizes": ["S", "M", "L", "XL"],
        "badge": None,
        "image": "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?q=80&w=1200&auto=format&fit=crop",
        "blurb": "Clean chino for weekend heat.",
    },
    {
        "id": "ps-012",
        "name": "Windhoek Cap",
        "price": 189,
        "compare_at": None,
        "category": "accessories",
        "gender": "accessories",
        "color": "black",
        "sizes": ["One size"],
        "badge": "New",
        "image": "https://images.unsplash.com/photo-1588850561407-ed78ebb80963?q=80&w=1200&auto=format&fit=crop",
        "blurb": "Structured six-panel cotton.",
    },
]


def get_product(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None


def filter_products(params):
    items = list(PRODUCTS)
    q = (params.get("q") or "").strip().lower()
    size = (params.get("size") or "").strip().lower()
    gender = (params.get("gender") or params.get("category") or "").strip().lower()
    category = (params.get("type") or "").strip().lower()
    color = (params.get("color") or "").strip().lower()
    price = (params.get("price") or "").strip()
    sale = params.get("sale")

    # Shop category pills: men/women/kids/accessories map to gender field
    if gender in {"men", "women", "kids", "accessories"}:
        items = [p for p in items if p["gender"] == gender]
    if category in {"tops", "bottoms", "accessories"}:
        items = [p for p in items if p["category"] == category]
    if color:
        items = [p for p in items if p["color"] == color]
    if size:
        size_label = size.upper() if size != "one size" else "One size"
        items = [p for p in items if size_label in p["sizes"] or size in [s.lower() for s in p["sizes"]]]
    if q:
        items = [p for p in items if q in p["name"].lower() or q in p["blurb"].lower()]
    if sale in {"1", "true", "yes"}:
        items = [p for p in items if p.get("compare_at")]
    if price == "0-250":
        items = [p for p in items if p["price"] <= 250]
    elif price == "250-500":
        items = [p for p in items if 250 < p["price"] <= 500]
    elif price == ">500":
        items = [p for p in items if p["price"] > 500]
    return items

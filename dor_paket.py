import json
from api_request import send_api_request, get_family

PACKAGE_FAMILY_CODE = "6fda76ee-e789-4897-89fb-9114da47b805"

def get_package_xut(api_key: str, tokens: dict):
    packages = []
    
    data = get_family(api_key, tokens, PACKAGE_FAMILY_CODE)
    package_variants = data["package_variants"]
    start_number = 1
    for variant in package_variants:
        if variant["name"] == "Dor Paket XL":
            for option in variant["package_options"]:
                if True:
                    friendly_name = option["name"]
                    
                    if friendly_name.lower() == "2.8gb":
                        friendly_name = "BONUS #TraktiranXL 28th Anniversary"
                        
                    packages.append({
                        "number": start_number,
                        "name": friendly_name,
                        "price": option["price"],
                        "code": option["package_option_code"]
                    })
                    
                    start_number += 1
    return packages
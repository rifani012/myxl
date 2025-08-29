import sys

from api_request import *
from ui import *
from util import load_token, ensure_api_key
from paket_xut import get_package_xut
from paket_sfy import get_package_sfy
from my_package import fetch_my_packages
from paket_custom_family import get_packages_by_family

user_data = {
    "is_logged_in": False,
    "phone_number": None,
    "balance": None,
    "balance_expired_at": None,
    "tokens": None,
}
        
        show_main_menu(user_data)
        
        choice = input("Pilih menu: ")
        # Logged in
        if user_data["is_logged_in"]:
            if choice == "1":
                print("Changing account...")
                phone_number = login_prompt()
                if phone_number:
                    user_data["phone_number"] = phone_number
                    continue
                else:
                    print("Failed to login. Please try again.")
                continue
            elif choice == "2":
                fetch_my_packages(api_key, user_data["tokens"])
                continue
            elif choice == "3":
                # XUT 
                packages = get_package_xut(api_key, user_data["tokens"])
                
                show_package_menu(api_key, user_data["tokens"], packages)
                continue
            elif choice == "4":
                family_code = input("Enter family code (or '99' to cancel): ")
                if family_code == "99":
                 continue
            elif choice == "5":
                # SFY 
                packages = get_package_sfy(api_key, user_data["tokens"])
                
                show_package_menu(api_key, user_data["tokens"], packages)
                get_packages_by_family(api_key, user_data["tokens"], family_code)
            elif choice == "99":
                print("Exiting the application.")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")
                pause()
        else:
            # Not logged in
            if choice == "1":
                phone_number = login_prompt()
                if phone_number:
                    user_data["phone_number"] = phone_number
                    continue
                else:
                    print("Failed to login. Please try again.")
                pause()
            elif choice == "99":
                print("Exiting the application.")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")
                pause()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting the application.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
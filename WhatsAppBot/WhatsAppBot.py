from Utilites.utilites import *

SUCCESS = 0
FAIL_LIST = []
CHROME_PATH = 'D:\Program Files (x86)\chromedriver.exe'


def intro():
    print('''
 __          ___           _                _____  _____    ____        _   
 \ \        / / |         | |         /\   |  __ \|  __ \  |  _ \      | |  
  \ \  /\  / /| |__   __ _| |_ ___   /  \  | |__) | |__) | | |_) | ___ | |_ 
   \ \/  \/ / | '_ \ / _` | __/ __| / /\ \ |  ___/|  ___/  |  _ < / _ \| __|
    \  /\  /  | | | | (_| | |_\__ \/ ____ \| |    | |      | |_) | (_) | |_ 
     \/  \/   |_| |_|\__,_|\__|___/_/    \_\_|    |_|      |____/ \___/ \__|
                                  
                                                        [@Made By: Tal Hasson]

-----------------------------------------------------------------------------------------
Please notice: after the browser has been launched come back and follow the instructions. 
-----------------------------------------------------------------------------------------                                                                           
''')


def prompt_user_for_contacts():
    user_choice = input('\nDo you want to load contacts from file or enter them manually?'
                        '\n[+] Press "1" for load from file'
                        '\n[+] Press "2" for manually\nChoice: ')
    while is_choice_valid(user_choice) is False:
        user_choice = input("[-] Not a valid option\nTry again: ")
    if user_choice == "1":
        contacts_list = get_contacts_from_file(CONTACTS_AND_MESSAGES_XLSX)
        if contacts_list is not False:
            return contacts_list
        else:
            contacts_list = get_user_contacts_using_prompt()
            return contacts_list

    else:
        contacts_list = get_user_contacts_using_prompt()
        return contacts_list


def send_message(contact):
    global SUCCESS
    wait = WebDriverWait(chrome_browser, 10)
    message = main_message + Keys.ENTER  # main message from user input or from a file
    message_box_xpath = '//div[@class="_3uMse"]'
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, message_box_xpath)))
    time.sleep(1)
    # sending the opening for the message and the main message(you can edit the opening as you want from here)
    input_box.send_keys(f"Hey {contact}, How are you? {message}")
    time.sleep(4)
    print(f"Successfully Send Message to: {contact}\n")
    SUCCESS += 1
    time.sleep(0.5)
    return SUCCESS


def search_contact_in_search_box(contact):
    wait_5 = WebDriverWait(chrome_browser, 5)

    search_box_path = '//div[@class="J3VFH"]'
    wait_5.until(EC.presence_of_element_located((By.XPATH, search_box_path)))
    input_search = chrome_browser.find_element_by_xpath('//div[@class= "_3FRCZ copyable-text selectable-text"]')
    time.sleep(0.5)
    chrome_browser.find_element_by_xpath('//button[@class="_3e4VU"]').click()
    input_search.clear()
    input_search.send_keys(contact)
    print('Contact Searched')
    time.sleep(4)


def search_contacts_and_send_messages(contacts_list):
    wait = WebDriverWait(chrome_browser, 10)
    wait_5 = WebDriverWait(chrome_browser, 5)
    contact_num = 1
    print("-----------------------------------------------------------------------------")
    scan_qr = input("\nScan the QR code and then press ENTER\n[*] if you are already in WhatsApp Web also press ENTER: ")
    while scan_qr != "":
        scan_qr = input("Just press ENTER to continue: ")
    for contact in contacts_list:
        print(f"\n{contact_num}. Contact name is: {contact}")
        contact_num += 1
        try:  # if contact is in recent chat list
            x_path = f'// span[ @ title = "{contact}"]'
            try:
                wait_5.until(EC.presence_of_element_located((By.XPATH, x_path)))
            except:
                search_contact_in_search_box(contact)

            chrome_browser.find_element_by_xpath(x_path).click()
            print("The contact Successfully Selected")
            time.sleep(2)
            send_message(contact)

        except:  # If contact Not found
            global FAIL_LIST
            print(f"Could`nt send message to: {contact}")
            FAIL_LIST.append(contact)
            pass

    chrome_browser.quit()


def print_results():
    print(f"\nSuccessfully Sent to: {SUCCESS}")
    print(f"Failed to Sent to: {len(FAIL_LIST)}")
    if len(FAIL_LIST) > 0:
        print(FAIL_LIST)


def is_url_get_request_valid(url):
    try:
        r = requests.get(url, timeout=3)
        r.raise_for_status()
        return True
    except requests.exceptions.HTTPError as httpE:
        print(f"HTTP Error: {httpE}")
        return False
    except requests.exceptions.ConnectionError as conE:
        print("Connection Error: try to check your internet connection.")
        return False
    except requests.exceptions.Timeout as timeoutE:
        print(f"Timeout Error: {timeoutE}")
        return False
    except requests.exceptions.RequestException as elseE:
        print(f"OOps: Something Else {elseE}")
        return False


def activate_whats_app_bot(url, contacts_list):
    if is_url_get_request_valid(url):
        chrome_browser.get(url)
        search_contacts_and_send_messages(contacts)
        print_results()
    else:
        print("[*] Quiting!")
        chrome_browser.quit()


if __name__ == '__main__':
    intro()
    contacts = prompt_user_for_contacts()
    main_message = get_message()
    options = webdriver.ChromeOptions()
    #options.add_argument("user-data-dir=C:\\*\\*\\AppData\\Local\\Google\\Chrome\\User Data\\")
    #options.add_argument("profile-directory=*")  # open costume chrome profile
    chrome_browser = webdriver.Chrome(executable_path=CHROME_PATH, options=options)
    activate_whats_app_bot('https://web.whatsapp.com', contacts)


from datetime import datetime

end_time = datetime(2022, 2, 7, 12, 36, 30)

sites_to_block = ['www.facebook.com', 'facebook.com']


hosts_path = r"C:\Windows\System32\drivers\etc\hosts"  # links this to the addresses to be blocked
# hosts_path = r"./hosts" it was test
redirect = "127.0.0.1"


def block_sites():
    if datetime.now() < end_time:
        print("block sites")
        with open(hosts_path, "r+") as hosts_files:
            hosts_content = hosts_files.read()
            for site in sites_to_block:
                if site not in hosts_content:
                    hosts_files.write(redirect + " " + site + "\n")
    else:
        print('unblock sites')
        with open(hosts_path, "r+") as hosts_files:
            lines = hosts_files.readlines()
            hosts_files.seek(0)   # sets the pointer to the beginning of the file
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hosts_files.write(line)
            hosts_files.truncate()


#if __name__ == "main":
    # Run the manually
    # Run in cron job
    # Run in the background using while True
 #   block_sites()

block_sites()
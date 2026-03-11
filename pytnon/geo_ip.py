import os
import requests
import geoip2.database
import json

DB_URL = "https://git.io/GeoLite2-Country.mmdb"
DB_FILE = "GeoLite2-Country.mmdb"
import socket


from urllib.parse import urlparse
import ipaddress

def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def check_and_download_db():
    if os.path.exists(DB_FILE) and os.path.getsize(DB_FILE) > 500000:
        return True
    
    print(f"Загрузка базы стран...")
    try:
        with requests.get(DB_URL, stream=True) as r:
            r.raise_for_status()
            with open(DB_FILE, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024*1024):
                    f.write(chunk)
        print("База успешно обновлена.")
        return True
    except Exception as e:
        print(f"Ошибка загрузки: {e}")
        return False

def get_country(ip):
    if not check_and_download_db():
        return "Ошибка: база данных недоступна."

    try:
        with geoip2.database.Reader(DB_FILE) as reader:
            response = reader.country(ip)
            return {
                "ip": ip,
                "country": response.country.name,
                "iso_code": response.country.iso_code,
                "continent": response.continent.name
            }
    except Exception as e:
        return f"Данные для {ip} не найдены или ошибка: {e}"

def get_flag(country_code):
    offset = ord('🇦') - ord('A')
    return "".join(chr(ord(c.upper()) + offset) for c in country_code)



if __name__ == "__main__":
    _path = "%AppData%\\Local\\nekoray\\config\\profiles"

    t = os.listdir(_path)
    for x in t:
        try:
        
            lo_path = _path + "\\" + x
            file = open(lo_path, "r")
            j = json.loads(file.read())
            file.close()
            ip = j['bean']['addr']

            result =""

            if check_ip(ip) != True:
                _ip = socket.gethostbyname(ip)
                result = get_country(_ip)
            else:
                result = get_country(ip)
            
            print(result)
            if j['bean']['name'] =="v2cross.com":
                j['bean']['name'] = get_flag(result["iso_code"]) + " " + result["continent"] + "_" + result["country"]

                file = open(lo_path, "w")
                json.dump(j, file)
                file.close()
        
            pass
        except Exception as e:
            pass
        else:
            pass
        finally:
            pass
    

    os.remove(DB_FILE)

    	
    	

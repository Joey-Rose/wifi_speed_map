import speedtest

source = "109.146.246.143"
s = speedtest.Speedtest(source_address=source)
servers = s.get_servers()

s.get_best_server()

print(s._best)

print(s.download(threads=None) / 1000000) 
print(s.upload(threads=None, pre_allocate=False) / 1000000) 
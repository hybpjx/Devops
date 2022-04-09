import subprocess


def ping(host):
    # ping 的ip 如果是up的很快 但如果是 down的 就会很慢
    result = subprocess.run(
        f'ping -c2 {host} &> /dev/null', shell=True
    )
    # return result
    # print(result)  # CompletedProcess(args='ping -c2 192.168.0.1 &> /dev/null', returncode=0)
    if result.returncode == 0:
        print(f"{host}:up")
    else:
        print(f"{host}:down")


if __name__ == '__main__':
    ip_list = ["192.168.0.{}".format(i) for i in range(1, 255)]
    for ip in ip_list:
        ping(ip)

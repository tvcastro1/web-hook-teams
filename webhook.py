import urllib3
import json
import csv

hook_url_nuclei = "https://2r7x21.webhook.office.com/webhookb2/c2ab9ea6-c70a-4c24-a482-95f3a00dc529@59f4759a-f8f0-4913-8d49-ffacce04f2ba/IncomingWebhook/86eae4e92689458eb5e6212a991010f9/237f722b-4e34-4430-ab3b-54176f464c6e"

class BotTeamsException(Exception):
    """custom exception for failed webhook call"""
    pass


class BotTeams(object):
    def __init__(self, hookurl, http_timeout=60):
        self.http = urllib3.PoolManager()
        self.payload = {}
        self.hookurl = hookurl
        self.http_timeout = http_timeout

    def text(self, mtext):
        self.payload["text"] = mtext
        return self

    def send(self):
        headers = {"Content-Type":"application/json"}
        r = self.http.request(
                'POST',
                f'{self.hookurl}',
                body=json.dumps(self.payload).encode('utf-8'),
                headers=headers, timeout=self.http_timeout)
        if r.status == 200: 
            return print(f'Status de retorno: {r.status}')
        else:
            raise BotTeamsException(r.reason)


if __name__ == "__main__":
    meuBotTeams = BotTeams(hook_url_nuclei)
    with open('vulnerabilidades.txt', 'r') as f:
        for line in f:
            meuBotTeams.text(line)
            meuBotTeams.send()




    
    

    



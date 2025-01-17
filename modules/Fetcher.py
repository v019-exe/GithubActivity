import requests
class Fetcher:
    def __init__(self, name):
        self.name = name
    
    
    def fetch(self):
        try:
            url =  f"https://api.github.com/users/{self.name}/events"
            response = requests.get(url)
            json = response.json()
            
            repos = []
            push_events = 0
            commits = 0
           
            for event in json:
               event_type = event["type"]
               if event_type == "PushEvent":
                   push_events += 1
               elif event_type == "CommitEvent":
                   commits += 1
               
               repos.append(event["repo"]["name"])
            
            print(f"Repositorios creados: {len(repos)}")
            print("Lista de repositorios creados:")
            for repo in repos:
                print(f"  - {repo}")

            print(f"Eventos de push: {push_events}")
            print(f"Total de commits: {commits}")
                    
        except Exception as e:
            print(e)


print(Fetcher("v019-exe").fetch())
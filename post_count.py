import requests
import time
from progress.bar import ChargingBar

class THW:
    def __init__(self, url):
        self.api_url = url
        
        # GLOBAL - CLASS - VARIABLES
        self.post_list_count = []
        self.posts = []
        self.total = 0
            
    def connect(self):
        possible_urls = [self.api_url]
        
        for page in range(0,1000):
            next_urls = self.api_url + '?page=' + str(page) 
            possible_urls.append(next_urls)

        try: 
            for idx, url in enumerate(possible_urls):
                response = requests.get(url,
                headers={"Accept": "application/json"},
                )
                data = response.json()
                blog_posts = data['posts']
                
                post_count = len(blog_posts)
                self.post_list_count.append(post_count)
                print(f"---- Getting Page {idx} Posts ---")
                
                for data in blog_posts:
                    article_title = data["title"]
                    pub_title = data["publication"]["title"]
                    domain = data["author"]["username"]
                    article_slug = domain + ".hashnode.dev/" + data["slug"]  
                    date_added = data["dateAdded"]
                    
                    self.posts.append((article_title, pub_title, article_slug, date_added))
                                
                if post_count == 0:
                    break  
            return "-- SUCCESSFULLY GOT ALL THE POSTS : SUMMARY IS READY ---"      
        except Exception as e:
            return f"ERROR :: {e}"
        
        
    # Get total count so far
    def count(self):
        self.connect()
        total_ = 0
        self.total = [total_ := total_ + x for x in self.post_list_count][-1]
        return f"There are currently {self.total} posts written!"
    
    # Print The Posts
    def posts(self):
        self.connect()
        for idx, post in enumerate(self.posts):            
            return idx, post               




        



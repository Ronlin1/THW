# Testing PyPI Upload after pip install
from thwAPI import thw

# print(dir(thw))

# initialize = thw.THW()

API_URLs = ['https://hashnode.com/api/feed/tag/thw-cloud-computing',
            'https://hashnode.com/api/feed/tag/thw-mobile-apps',
            'https://hashnode.com/api/feed/tag/thw-web3',
            'https://hashnode.com/api/feed/tag/thw-web-apps'
            
            ]


# for idx, url in enumerate(API_URLs):
#     print(f"API {idx} ; Counter")
#     count = thw.THW(url).count()
#     print(count)
    
"""
Estimated Count At the time of execution;
...

Cloud Computing; There are currently 81 posts written!
Mobile Apps ; There are currently 73 posts written!
Web 3 ; There are currently 99 posts written!
Web Apps ; There are currently 264 posts written!
...

""" 
       
for idx, url in enumerate(API_URLs):
    print(f"API {idx} ; Summary")
    summary = thw.THW(url).all_posts()
    print(summary)
      

        
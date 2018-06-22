# dynamic-WebCrawler

I tried to fetch a webpage written in React.
Then I found selenium can help me do this.
The theorem is that selenium can automatically open a browser and automatically "use" it.
So we can wait the browser until it finish rendering the components, and we can successfully get the content in some componenent we want.
So I successfully done it.
But at the end I Had no need to fetch the React webpage, I turned to fetch another dynamic page( but simpler than React).


udn.py
It's a web-crawler using selenium to automatically scroll the page to load enough numbers of news.
"my_url" is the news list in udn.com in some catagory.
Before you use it, you need to download a driverFile for firefox or chrome.
selenium will open a driver (firefox or chrome) and open the page, and fetch link and scroll down and fetch link... 
After fetch all news links we need, use BeautifulSoup to get content you need. ( also can use selenium) 
Then get the specific block you needs, and Output it in JSON.




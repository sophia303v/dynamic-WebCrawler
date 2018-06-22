# dynamic-WebCrawler

I tried to fetch a webpage written in React. <br>
Then I found selenium can help me do this.<br>
The theorem is that selenium can automatically open a browser and automatically "use" it. <br>
So we can wait for the browser until it finishes rendering the components, and we can successfully get the content in some components we want. <br>
So I successfully did it.  <br>
But at the end I Had no need to fetch the React webpage, I turned to fetch another dynamic page( but simpler than React).  <br>

<h3> udn.py  </h3>
It's a web-crawler using selenium to automatically scroll the page to load enough numbers of news. <br>
"my_url" is the news list in udn.com in some category. <br>
Before you use it, you need to download a driver file for firefox or chrome.  <br>
selenium will open a driver (firefox or chrome) and open the page, and fetch link and scroll down and fetch link...  <br>
After fetching all news links we need, use BeautifulSoup to get content you need. ( also can use selenium)  <br>
Then get the specific block you need, and output it in JSON. <br>

<h3> mobile01.py </h3>
It's a simple static web-crawler. Fetch the data in udn. Use beautifulSoup. Output as JSON. <br>
BeautifulSoup will have a stange problem that it will disconnected sometimes. <br>
If it disconnected, just look the articlesNum printed on console. And modified the "articleNum" parameter in this file
and then it can continue to fetch the next following articles. <br>

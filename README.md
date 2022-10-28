# dynamic-WebCrawler

When I tried to fetch a webpage using React, I found selenium can help me do this.<br>
The mechanism is that selenium can automatically open a browser and "use" it. <br>
Hence, we can wait for the browser until it finishes rendering the components. We can successfully get the content in those components we want. <br>
However, at the end I turned to fetch another dynamic page which using simpler language than React. XD <br>

<h3> udn.py  </h3>
It's a web-crawler using selenium to automatically scroll the page to load enough numbers of news. <br>
"my_url" is the news list in udn.com in some category. <br>
Before using it, we need to download a driver file for firefox or chrome.  <br>
Selenium will open a driver (firefox or chrome) and open the page, and fetch link and scroll down and fetch link...  <br>
After fetching all links of news we need, use BeautifulSoup to get content you need. (can also use selenium)  <br>
Then get the specific block you need, and output it in JSON. <br>

<h3> mobile01.py </h3>
It's a simple static web-crawler. Fetch the data in mobile01. Use beautifulSoup. Output as JSON. <br>
I encounter strange problems when using BeautifulSoup. It will disconnect sometimes. <br>
If it disconnected, just read the articlesNum printed on console and modified the "articleNum" parameter in this file.
Then, it can continue to fetch the next following articles. <br>

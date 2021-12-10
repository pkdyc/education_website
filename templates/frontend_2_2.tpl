<link rel="stylesheet" type="text/css" href="css/tutorial.css">

<div class="tutorial-container">
	<div class="nav-div">
		<ul class="nav-list">
			<li class="nav-title">
				<h3>CHAPTER 3 
				<h4>FRONTEND
			</li>
			<li class="nav-li">
				<a href="/frontend/intro">1. Frontend Introduction</a>
			</li>
			<li class="nav-li">
				<a href="/frontend/html">2. HTML</a>
				<ul>
					<li class="nav-li">
						<a href="/frontend/html/element">2a. HTML elements</a>
					</li>
					<li class="nav-li">
						<a href="/frontend/html/structure" style="background-color: #111;">2b. HTML structure</a>
					</li>
				</ul>
			</li>
			<li class="nav-li">
				<a href="/frontend/css">3. CSS</a>
				<ul>
					<li class="nav-li">
						<a href="/frontend/css/syntax">3a. CSS Syntax</a>
					</li>
				</ul>
			</li>
			<li class="nav-li">
				<a href="/frontend/js">4. JavaScript</a>
				<ul>
					<li class="nav-li">
						<a href="/frontend/js/guideline">4a. JavaScript Guideline</a>
					</li>
					<li class="nav-li">
						<a href="/frontend/js/extension">4b. JavaScript Extension</a>
					</li>
				</ul>
			</li>
			<li class="nav-li">
				<a href="/summary">5. Summary</a>
			</li>
		</ul>
	</div>
	<div class="content-div">

		<dl>
			<dt>
				<h1>HTML structure</h1>
			</dt>

			<dt>
				<h2>Anatomy of an HTML document</h2>
			</dt>

			<dd>
				<img src="img/html_structure.png" alt="HTML structure">
			</dd>

			<dt>
				<h4>It looks like this in the browser: </h4>
			</dt>
			<dd>
				<img src="img/html_structure_demo.png" alt="HTML structure demo">
			</dd>

			<dt>
				<h4>In this example, we have: </h4>
			</dt>

			<dt>1. &lt;!DOCTYPE html&gt;:</dt>
			<dd>
				The doctype. When HTML was young (1991-1992), doctypes were meant to act as links to a set of rules that the
				HTML page had to follow to be considered good HTML. Doctypes used to look something like this:
				<br><br>
				&nbsp;&nbsp;&lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
				"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"&gt;
				<br><br>
				More recently, the doctype is a historical artifact that needs to be included for everything else to work
				right. &lt;!DOCTYPE html&gt; is the shortest string of characters that counts as a valid doctype. That is
				all you need to know!
			</dd>

			<br><br>

			<dt>2. &lt;html&gt;</dt>
			<dd>
				This element wraps all the content on the page. It is sometimes known as the root element.
			</dd>

			<br><br>

			<dt>3. &lt;head&gt;&lt;\head&gt;</dt>
			<dd>
				The &lt;head&gt; element. This element acts as a container for everything you want to include on the HTML page, that isn't the content the page will show to viewers. This includes keywords and a page description that would appear in search results, CSS to style content, character set declarations, and more. You'll learn more about this in the next article of the series.
			</dd>

			<br><br>

			<dt>4. &lt;meta charset="utf-8"&gt;</dt>
			<dd>
				This element specifies the character set for your document to UTF-8, which includes most characters from the vast majority of human written languages. With this setting, the page can now handle any textual content it might contain. There is no reason not to set this, and it can help avoid some problems later.
			</dd>

			<br><br>

			<dt>5. &lt;title&gt;&lt;\title&gt;</dt>
			<dd>
				The &lt;title&gt; element. This sets the title of the page, which is the title that appears in the browser tab the page is loaded in. The page title is also used to describe the page when it is bookmarked.
			</dd>

			<br><br>

			<dt>6.  &lt;body&gt;&lt;\body&gt;</dt>
			<dd>
				This contains all the content that displays on the page, including text, images, videos, games, playable audio tracks, or whatever else.
			</dd>

			<br><br>

			<dt><h3>By now you have learnt the basic layout of a HTML file, in order to write a simple web page, simply do these 2 steps: </h3></dt>

			<dd>1. Write a basic HTML structure similar to the above one</dd>
			<dd>2. Put elements at where you want it to be</dd>

			<br>

			<dt><h3>Now lets go a step further, given the following layout, write a HTML for it</h3></dt>
			<dd><img src="img/html_layout.png" alt="HTML layout example"></dd>

			<br>

			<dd><h4>You probably will write something like this: </h4></dd>
			<dd><img src="img/html_layout_demo.png" alt="HTML layout demo"></dd>
			<dd><h4>And the output looks like this: </h4></dd>
			<dd><img src="img/html_layout_result.png" alt="HTML layout result"></dd>

			<dd><h4>Notice that "Index" section and "Content" section are in different rows</h4></dd>
			<dd><h4>But we want them to be in the same row side by side</h4></dd>

			<br>

			<dd><h3>This is where CSS kicks in, now lets find out what is CSS and how does it solve this problem</h3></dd>
		</dl>

		<div style="float: right; text-align: center; padding: 20px; margin-right: 30px;">
			<div class="btn-1">
				<a href="/frontend/css"><span>Learn CSS</span></a>
			</div>
		</div>
		

		<p>
		</p>

	</div>
</div>
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
						<a href="/frontend/html/structure">2b. HTML structure</a>
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
						<a href="/frontend/js/guideline" style="background-color: #111;">4a. JavaScript Guideline</a>
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
		<h1>JavaScript Guideline</h1>
		<dl>
			<dt><h2>Before we start, let's learn how to apply JavaScript in our HTML file</h2></dt>
			<dt><h2>So how do you add JavaScript to your page?</h2></dt>
			<dd></dd>
			<dt>1. Internal JavaScript --- Write JavaScript inside HTML file</dt>
				<dd>a. Add the following code into your header section, right before the closing tag for head</dd>
				<dd><img src="img/add-js-1.png" alt="add-js-1"></dd>
				<dd>b. Then write your JavaScript code inside</dd>
			<br>
			<dt>2. External JavaScript --- Write JavaScript outside HTML file</dt>
				<dd>a. Create an independent js file</dd>
				<dd>b. Add the folling code to the same place as above</dd>
				<dd>&nbsp;&nbsp;&nbsp;&nbsp;&lt;script src="/path/to/your/js-file"&gt;&lt;/script&gt;</dd>

			<dt><h2>Now let's start with a simple example</h2></dt>

			<dt>HTML</dt>
			<br>
			<dd>
				<img src="img/js_demo_html.png" alt="js_demo_html">
			</dd>
			<dd><p>Player 1: Chris</p></dd>
			<br>
			<dt>CSS</dt>
			<br>
			<dd>
				<img src="img/js_demo_css.png" alt="js_demo_css">
			</dd>
			<dd><p id="js_demo_para_1">Player 1: Chris</p></dd>
			<br>
			<dt>JavaScript</dt>
			<br>
			<dd>
				<img src="img/js_demo_js.png" alt="js_demo_js">
			</dd>
			<dd><p id="js_demo_para_2">Player 1: Chris</p></dd>
			<script>
				const para = document.getElementById("js_demo_para_2");
				para.addEventListener('click', updateName, false);
				function updateName() {
					let name = prompt('Enter a new name');
					para.innerHTML = 'Player 1: ' + name;
				}
			</script>
			<dt><h4>Click on the last "Player: Chris" to see how it works</h4></dt>

			<br>
			<dt><h2>So what can JavaScript really do?</h2></dt>
			<dt>The core client-side JavaScript language consists of some common programming features that allow you to do things like:</dt>
			<br>
			<dt>1. Store useful values inside variables.</dt>
			<dd><img src="img/boxes.png" alt="js-variables"></dd>
			<dd>In the above example for instance, we ask for a new name to be entered then store that name in a variable called name.</dd>
			<dd>Before 2015, using the "var" keyword was the only way to declare a JavaScript variable.</dd>
			<dd>The 2015 version of JavaScript (ES6) allows the use of the "const" keyword to define a variable that cannot be reassigned, and the "let" keyword to define a variable with restricted scope.</dd>
			<br>
			<dt>2. Operations on pieces of text (known as "strings" in programming).</dt>
			<dd>In the above example we take the string "Player 1: " and join it to the name variable to create the complete text label, e.g. ''Player 1: Chris".</dd>
			<dd>In JavaScript, document.getElementById(), document.getElementsByClassName() are commonly used to fetch target element(s)</dd>
			<dd>Once we fetch the element, we are able to change things like the value it contains or the property it has</dd>
			<br>
			<dt>3. Running code in response to certain events occurring on a web page.</dt>
			<dd>We used a click event in our example above to detect when the button is clicked and then run the code that updates the text label.</dd>
			<dd>In JavaScript, click event is the most common event that would need to be processed, we can either create a Listener as described above, or simply user property "onclick" and pass a function to it to execute</dd>
			<br>
			<dt>And much more!</dt>

			<dt>So base on what we've just learnt, JavaScript can program the behavior of web pages base on these 2 steps</dt>
			<dd>Step1: Fetch element</dd>
			<dd>Step2: Perform actions on elements (e.g. change value)</dd>

			<p>What is even more exciting however is the functionality built on top of the client-side JavaScript language. So-called Application Programming Interfaces (APIs) provide you with extra superpowers to use in your JavaScript code.</p>
			<p>APIs are ready-made sets of code building blocks that allow a developer to implement programs that would otherwise be hard or impossible to implement. They do the same thing for programming that ready-made furniture kits do for home building — it is much easier to take ready-cut panels and screw them together to make a bookshelf than it is to work out the design yourself, go and find the correct wood, cut all the panels to the right size and shape, find the correct-sized screws, and then put them together to make a bookshelf.</p>
		
			<dt><h2>What is JavaScript doing on your page?</h2></dt>
			<p>Let's briefly recap the story of what happens when you load a web page in a browser (first talked about in our How CSS works article). When you load a web page in your browser, you are running your code (the HTML, CSS, and JavaScript) inside an execution environment (the browser tab). This is like a factory that takes in raw materials (the code) and outputs a product (the web page).</p>
			<dd><img src="img/web-execution.png" alt="web-execution"></dd>
			<p>A very common use of JavaScript is to dynamically modify HTML and CSS to update a user interface, via the Document Object Model API (as mentioned above). Note that the code in your web documents is generally loaded and executed in the order it appears on the page. If the JavaScript loads and tries to run before the HTML and CSS it is affecting has been loaded, errors can occur. You will learn ways around this later in the article, in the Script loading strategies section.</p>
			
		</dl>

		<div style="float: right; text-align: center; padding: 20px; margin-right: 30px;">
			<div class="btn-1">
				<a href="/frontend/js/extension"><span>JavaScript Extension</span></a>
			</div>
		</div>

	</div>
</div>
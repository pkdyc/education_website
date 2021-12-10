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
                        <a href="/frontend/html/element" style="background-color: #111;">2a. HTML elements</a>
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
				<h1>HTML elements</h1>
			</dt>

            <dt>
				<h2>Anatomy of an HTML element</h2>
			</dt>
            <dd><img src="img/html_element.png" alt="HTML element"></dd>
            <br>
            <dt><h3>The anatomy of our element is:</h3></dt>
            <dt>The opening tag:</dt>
            <dd> 
                This consists of the name of the element (in this example, p for paragraph), wrapped in opening and closing angle brackets. 
                <br>
                This opening tag marks where the element begins or starts to take effect. In this example, it precedes the start of the paragraph text.
            </dd>
            <br>
            <dt>The content:</dt>
            <dd>
                This is the content of the element. In this example, it is the paragraph text.
            </dd>
            <br>
            <dt>The closing tag:</dt>
            <dd>
                This is the same as the opening tag, except that it includes a forward slash before the element name. 
                <br>
                This marks where the element ends. Failing to include a closing tag is a common beginner error that can produce peculiar results.
            </dd>
            <br>
                The element is the opening tag, followed by content, followed by the closing tag.
            <br>

            <dt><h4>Examples</h4></dt>
            <dd>&lt;div&gt; This is a div container&lt;/div&gt;</dd>
            <dd>&lt;p&gt; This is a paragraph&lt;/p&gt;</dd>
            <dd>&lt;img&gt; This is an image&lt;/img&gt;</dd>
            <dt><h4>Common elements</h4></dt>
            <dd><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element">HTML Elements Reference</a></dd>

            <dt>
                <h2>Attributes</h2>
            </dt>
            <dd><img src="img/html_element_attribute.png" alt="HTML element attribute"></dd>
            <br>
            <dt><h4>An attribute should have:</h4></dt>
            <dd>A space between it and the element name. (For an element with more than one attribute, the attributes should be separated by spaces too.)</dd>
            <dd>The attribute name, followed by an equal sign.</dd>
            <dd>An attribute value, wrapped with opening and closing quote marks.</dd>
            <br>

            <dt><h4>Examples</h4></dt>
            <dd>&lt;p class="myClassName"&gt; This is a paragraph&lt;/p&gt;</dd>
            <dd>&lt;img src="/path/to/img" onclick="myJsFunction"&gt; This is an image&lt;/img&gt;</dd>

            <dt><h4>Common attributes</h4></dt>
            <dd><a href="https://www.w3schools.com/tags/ref_attributes.asp">HTML Attributes Referenc</a></dd>
        </dl>

        <div style="float: right; text-align: center; padding: 20px; margin-right: 30px;">
			<div class="btn-1">
				<a href="/frontend/html/structure"><span>Learn HTML structure</span></a>
			</div>
		</div>

		<p>

		</p>

	</div>
</div>
markdownHtml = """
<h1 id="blog-api-documentation">Blog API Documentation</h1>
<h2 id="setup">Setup</h2>
<h3 id="clone-the-repository-and-install-all-the-dependancies-listed-in-requirements-txt-">Clone the repository and install all the dependancies listed in <code>requirements.txt</code></h3>
<pre><code>pip <span class="hljs-keyword">install</span> -r requirements.txt
</code></pre><h3 id="perform-database-migrations">Perform database migrations</h3>
<pre><code>python manage<span class="hljs-selector-class">.py</span> makemigrations
python manage<span class="hljs-selector-class">.py</span> migrate
</code></pre><h3 id="run-development-server">Run development server</h3>
<pre><code>python manage<span class="hljs-selector-class">.py</span> runserver
</code></pre><h3 id="creating-the-super-user-to-access-django-admin">Creating the super user to access django admin</h3>
<pre><code>python manage<span class="hljs-selector-class">.py</span> createsuperuser
</code></pre><h2 id="api-documentation">API Documentation</h2>
<h3 id="creating-or-registering-user">Creating or registering user</h3>
<p>Send post request to <code>http://127.0.0.1:8000/api/users/register/</code> with json data</p>
<pre><code>{
    <span class="hljs-attr">"username"</span>:<span class="hljs-string">"karun"</span>,
    <span class="hljs-attr">"email"</span>:<span class="hljs-string">"karun@gmail.com"</span>,
    <span class="hljs-attr">"password"</span>:<span class="hljs-string">"password"</span>
}
</code></pre><h3 id="getting-jwt-token">Getting jwt token</h3>
<p>To get jwt token send a POST request to <code>http://127.0.0.1:8000/api/users/authenticate/</code> with login credentials as json data.</p>
<pre><code>{
    <span class="hljs-attr">"username"</span>:<span class="hljs-string">"karun"</span>,
    <span class="hljs-attr">"password"</span>:<span class="hljs-string">"password"</span>
}
</code></pre><h3 id="list-all-blogs">List all blogs</h3>
<p>To list all blogs, send GET request to <code>http://127.0.0.1:8000/api/blogs</code>. Response would look like</p>
<pre><code>{
    <span class="hljs-attr">"message"</span>: [
        {
            <span class="hljs-attr">"id"</span>: <span class="hljs-number">2</span>,
            <span class="hljs-attr">"title"</span>: <span class="hljs-string">"Test2"</span>,
            <span class="hljs-attr">"content"</span>: <span class="hljs-string">"test"</span>,
            <span class="hljs-attr">"created_at"</span>: <span class="hljs-string">"2023-08-21T15:50:30.891199Z"</span>,
            <span class="hljs-attr">"updated_at"</span>: <span class="hljs-string">"2023-08-21T14:52:49.950486Z"</span>,
            <span class="hljs-attr">"auther"</span>: <span class="hljs-number">2</span>,
            <span class="hljs-attr">"comments"</span>: []
        },
        {
            <span class="hljs-attr">"id"</span>: <span class="hljs-number">3</span>,
            <span class="hljs-attr">"title"</span>: <span class="hljs-string">"test content"</span>,
            <span class="hljs-attr">"content"</span>: <span class="hljs-string">"test content"</span>,
            <span class="hljs-attr">"created_at"</span>: <span class="hljs-string">"2023-08-21T15:25:10.050163Z"</span>,
            <span class="hljs-attr">"updated_at"</span>: <span class="hljs-string">"2023-08-21T15:25:10.050163Z"</span>,
            <span class="hljs-attr">"auther"</span>: <span class="hljs-number">1</span>,
            <span class="hljs-attr">"comments"</span>: []
        },
        {
            <span class="hljs-attr">"id"</span>: <span class="hljs-number">4</span>,
            <span class="hljs-attr">"title"</span>: <span class="hljs-string">"test content2"</span>,
            <span class="hljs-attr">"content"</span>: <span class="hljs-string">"test content2"</span>,
            <span class="hljs-attr">"created_at"</span>: <span class="hljs-string">"2023-08-21T18:27:45.191349Z"</span>,
            <span class="hljs-attr">"updated_at"</span>: <span class="hljs-string">"2023-08-21T15:31:04.272362Z"</span>,
            <span class="hljs-attr">"auther"</span>: <span class="hljs-number">1</span>,
            <span class="hljs-attr">"comments"</span>: [
                <span class="hljs-number">4</span>,
                <span class="hljs-number">5</span>
            ]
        }
    ]
}
</code></pre><h3 id="creating-blog">Creating blog</h3>
<p>This is a protected route. To create a blog user should be registered. POST request to <code>http://127.0.0.1:8000/api/blogs/</code> should include jwt token in headers as <code>Authorization &lt;jwt token&gt;</code>. Request body would look like </p>
<pre><code>{
    <span class="hljs-attr">"title"</span>:<span class="hljs-string">"new blog"</span>,
    <span class="hljs-attr">"content"</span>:<span class="hljs-string">"content of new blog"</span>
}
</code></pre><h3 id="updating-a-blog">Updating a blog</h3>
<p>A blog can only be updated by its author. To update a blog send a PUT request to <code>http://127.0.0.1:8000/api/blogs/&lt;blog_id&gt;/</code> with jwt token at the header. Request body would look like</p>
<pre><code>{
    <span class="hljs-attr">"title"</span>:<span class="hljs-string">"new title"</span>,
    <span class="hljs-attr">"content"</span>:<span class="hljs-string">"new content"</span>
}
</code></pre><p>NOTE : Replace <code>&lt;blog_id&gt;</code> with valid blog id</p>
<h3 id="deleting-a-blog">Deleting a blog</h3>
<p>A blog can only be deleted by its author. To delete a blog send a DELETE request to <code>http://127.0.0.1:8000/api/blogs/&lt;blog_id&gt;/</code> with jwt token at the header.</p>
<p>NOTE : Replace <code>&lt;blog_id&gt;</code> with valid blog id</p>
<h3 id="list-all-comments-of-a-particular-blog-">List all comments of a particular blog.</h3>
<p>To list all blogs, send GET request to <code>http://127.0.0.1:8000/api/comments/&lt;blog_id&gt;</code>.  <code>&lt;blog_id&gt;</code> is the id of the blog for which you want to list the comments. Response would look like</p>
<pre><code>{
    <span class="hljs-attr">"message"</span>: [
        {
            <span class="hljs-attr">"id"</span>: <span class="hljs-number">4</span>,
            <span class="hljs-attr">"content"</span>: <span class="hljs-string">"new content new content"</span>,
            <span class="hljs-attr">"created_at"</span>: <span class="hljs-string">"2023-08-21T18:24:49.375267Z"</span>,
            <span class="hljs-attr">"updated_at"</span>: <span class="hljs-string">"2023-08-21T18:23:12.810339Z"</span>,
            <span class="hljs-attr">"auther"</span>: <span class="hljs-number">1</span>
        },
        {
            <span class="hljs-attr">"id"</span>: <span class="hljs-number">5</span>,
            <span class="hljs-attr">"content"</span>: <span class="hljs-string">"new content new new jdfjdfj dfjdkjfcontent"</span>,
            <span class="hljs-attr">"created_at"</span>: <span class="hljs-string">"2023-08-21T18:28:42.408071Z"</span>,
            <span class="hljs-attr">"updated_at"</span>: <span class="hljs-string">"2023-08-21T18:27:45.176316Z"</span>,
            <span class="hljs-attr">"auther"</span>: <span class="hljs-number">3</span>
        }
    ]
}
</code></pre><h3 id="creating-a-comment">Creating a  comment</h3>
<p>This is a protected route. To create a comment, user should be registered. POST request to <code>http://127.0.0.1:8000/api/comments/</code> should include jwt token in headers as <code>Authorization &lt;jwt token&gt;</code>. Request body would look like </p>
<pre><code>{
    <span class="hljs-attr">"content"</span>:<span class="hljs-string">"blog is very informative."</span>,
    <span class="hljs-attr">"blog_id"</span>: <span class="hljs-number">4</span>
}
</code></pre><h3 id="updating-a-comment">Updating a comment</h3>
<p>A blog can only be updated by its author. To update a blog send a PUT request to <code>http://127.0.0.1:8000/api/comments/&lt;comment_id&gt;/</code> with jwt token at the header. Request body would look like</p>
<pre><code>{
    <span class="hljs-attr">"content"</span>:<span class="hljs-string">"This blog is life saver for me!!"</span>
}
</code></pre><p>NOTE : Replace <code>&lt;comment_id&gt;</code> with valid comment id</p>
<h3 id="deleting-a-comment">Deleting a comment</h3>
<p>A comment can only be deleted by its author. To delete a blog send a DELETE request to <code>http://127.0.0.1:8000/api/comments/&lt;comment_id&gt;/</code> with jwt token at the header.</p>
<p>NOTE : Replace <code>&lt;commet_id&gt;</code> with valid comment id</p>
"""
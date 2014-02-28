<html>
<body>

<article>
<h1>
<a name="some-important-steps" class="anchor" href="#some-important-steps"><span class="octicon octicon-link"></span></a>Some Important Steps</h1>

<h2>
<a name="before-your-work" class="anchor" href="#before-your-work"><span class="octicon octicon-link"></span></a>Before your work</h2>

<p>$ git checkout master</p>

<p>$ git pull origin master:master</p>

<p>$ git checkout 'yourbranch'</p>

<p>$ git merge master</p>

<p>// now you are in your up-to-date local repo</p>

<h2>
<a name="during-your-work" class="anchor" href="#during-your-work"><span class="octicon octicon-link"></span></a>During your work</h2>

<p>// if you want to commit your local repo, make sure you stay in yourbranch</p>

<p>$ git add 'somefiles'</p>

<p>$ git commit -m "'description of this commit'"</p>

<h2>
<a name="finish-your-work" class="anchor" href="#finish-your-work"><span class="octicon octicon-link"></span></a>Finish your work</h2>

<p>// make sure you already commit your local repo and stay in yourbranch</p>

<p>$ git push origin 'yourbranch':'yourbranch'</p></article>

  </body>
</html>


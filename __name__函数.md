---


---

<h1 id="name__函数的作用">__name__函数的作用</h1>
<p>常在脚本里面看到下面这段代码：</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">if</span> __name__ <span class="token operator">==</span> <span class="token string">'__main__'</span><span class="token punctuation">:</span>
    main<span class="token punctuation">(</span><span class="token punctuation">)</span>
</code></pre>
<h3 id="这个name到底是用来干什么的呢？">这个name到底是用来干什么的呢？</h3>
<p>其实他是Python里面的一个内置变量（前后各有两个下划线）他有两个可能的值</p>
<ul>
<li>当直接执行一段脚本的时候，这段脚本的__ name __变量就等于__main __</li>
<li>当这段脚本被导入到其他程序中的时候，这段脚本的__ name __变量就等于脚本本身的名字</li>
</ul>
<p>举个例子，假设我们有一个叫<strong><a href="http://nameScript.py">nameScript.py</a></strong>的脚本，如下</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">def</span> <span class="token function">myFunction</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">'变量 __name__ 的值是 '</span> <span class="token operator">+</span> __name__<span class="token punctuation">)</span>
<span class="token keyword">def</span> <span class="token function">main</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
    myFunction<span class="token punctuation">(</span><span class="token punctuation">)</span>
<span class="token keyword">if</span> __name__ <span class="token operator">==</span> <span class="token string">'__main__'</span><span class="token punctuation">:</span>
    main<span class="token punctuation">(</span><span class="token punctuation">)</span>
</code></pre>
<h3 id="情况-1-直接运行脚本">情况 1 直接运行脚本</h3>
<p>当我们直接执行<strong><a href="http://nameScript.py">nameScript.py</a></strong>的时候，流程是这样的：<br>
<img src="https://lh3.googleusercontent.com/21Op5ToB9e551fzvMLlaAobu7_NgB---sXbPdQq4HT4HHmpbtXHQPfqZEtZ8P1VT7oq7A-Unu4zL" alt="" title="name变量"></p>
<p>在所有其他代码执行之前，__name__变量就被设置为   _<em>main</em> _ 了。在此之后，通过执行 def 语句，函数  <strong>main()</strong>  和  <strong>myFunction()</strong>  的本体被载入。</p>
<p>接着，因为这个 if 语句后面的表达式为真  <strong>true</strong>，函数  <strong>main()</strong>  就被调用了。而 main() 函数又调用了<strong>myFunction()</strong>，打印出变量的值__main_ _。</p>
<h3 id="情况2--从其他脚本里导入">情况2  从其他脚本里导入</h3>
<p>如果你需要在其他脚本里重用这个 <strong>myFunction()</strong> 函数，比如在 <strong><a href="http://importingScript.py">importingScript.py</a></strong> 里，我们可以将 <strong><a href="http://nameScript.py">nameScript.py</a></strong> 作为一个模组导入。<br>
这时，我们就有了两个不同的作用域：一个是 <strong>importingScript</strong> 的，一个是 <strong>nameScript</strong> 的。<br>
<img src="https://lh3.googleusercontent.com/Yw7aWVvE75NGN_zVkrUWs7M2X0XbmobMS2YFcdVxnRxaGvrZJEAkrThOgVME3aqGunOS-JmT9iso" alt="enter image description here"><br>
在  <strong><a href="http://importingScript.py">importingScript.py</a></strong>  里，<strong><strong>name</strong></strong>  变量就被设置为  <strong>‘<strong>main</strong>’</strong>。当导入  <strong>nameScript</strong>  的时候，Python 就在本地和环境变量  <strong>PATH</strong>  指向的路径中寻找对应名称的 .py 文件，找到之后，将会运行导入的文件中的代码。</p>
<p>但这一次，在导入的时候，它自身的  <strong><strong>name</strong></strong>  变量就被设置为了  <strong>‘nameScript’</strong>，接下来还是一样，函数  <strong>main()</strong>  和  <strong>myFunction()</strong>  的本体被载入。然而，这一次 if 语句后面的表达式结果为假 false，所以  <strong>main()</strong>  函数没有被调用。</p>
<p>导入完毕之后，回到  <strong><a href="http://importingScript.py">importingScript.py</a></strong>  中。现在  <strong>nameScript</strong>  模块中的函数定义已经被导入到当前的作用域中，于是我们通过  <strong>ns.myFunction()</strong>  的方式调用模块中的函数，这个函数返回的是模块内的变量的值  <strong>‘nameScript’</strong>。</p>


# make_tags
**Topic:** 



The web is built with HTML strings like "&lt;i&gt;Yay&lt;/i&gt;" which draws Yay as italic text. In this example, the "i" tag makes &lt;i&gt; and &lt;/i&gt; which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "&lt;i&gt;Yay&lt;/i&gt;".

<code>
make_tags("i", "Yay") → "&lt;i&gt;Yay&lt;/i&gt;"
make_tags("i", "Hello") → "&lt;i&gt;Hello&lt;/i&gt;"
make_tags("cite", "Yay") → "&lt;cite&gt;Yay&lt;/cite&gt;"
</code>

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p147483) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def make_tags(tag: str, word: str) -> str:
```

## Tests
```python
from main import make_tags


def test_make_tags_1():
    assert make_tags('i', 'Yay') == '<i>Yay</i>'


def test_make_tags_2():
    assert make_tags('i', 'Hello') == '<i>Hello</i>'


def test_make_tags_3():
    assert make_tags('cite', 'Yay') == '<cite>Yay</cite>'


def test_make_tags_4():
    assert make_tags('address', 'here') == '<address>here</address>'


def test_make_tags_5():
    assert make_tags('body', 'Heart') == '<body>Heart</body>'


def test_make_tags_6():
    assert make_tags('i', 'i') == '<i>i</i>'


def test_make_tags_7():
    assert make_tags('i', '') == '<i></i>'
```

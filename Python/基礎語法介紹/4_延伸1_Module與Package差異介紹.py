"""
Python 提供的 module（模組）與 package（套件）是建立架構的基本元件
但在module之間為了重複使用一些 function（函數）或 class（類別）而必須互相 import（匯入），使用上一個不注意就會掉入混亂的 import 陷阱

Module與Package
基本上一個檔案就是一個 module，裡頭可以定義 function，class，和 variable
把一個 module 想成一個檔案，那一個package就是一個目錄了。Package 可裝有 subpackage 和 module，讓你的專案更條理更組織化，最後打包好還能分給別人使用
"""

"""
這邊先解釋module：
假設有一個 module sample_module.py 裡頭定義了一個 function sample_func，如下：
"""
def sample_func():
    print('Hello!')


"""
現在你在同一個目錄裡下有另一個 module sample_module_import.py 想要重複使用這個 function，這時可以直接從 sample_module import 拿取，如下：
"""
from sample_module import sample_func
if __name__ == '__main__':
    sample_func()

"""
再來解釋package：
若把上面兩個檔案包在一個新的目錄sample_package，底下有以下檔案：
sample_package/
├── __init__.py
├── sample_module.py
└── sample_module_import.py

很重要的是新增那個 __init__.py 檔。檔案是空的沒關係，但一定要有，有點宣稱自己是一個 package 的味道

這時候如果是進到 sample_package 裡面跑一樣的指令，那沒差
但既然都打包成 package 了，通常是在整個專案的其他地方需要用到的時候 import 它，這時候裡面的 import 就要稍微做因應
此時就需要修正一下 sample_package/sample_module_import.py

利用以下幾種不同的 import 寫法修改，這時我們在跟 sample_package 同一個 folder 底下執行下面兩種指令，不同的import寫法及指令，會有不同的結果
指令 1. python3 sample_package/sample_module_import.py
指令 2. python3 -m sample_package.sample_module_import

# 不標準的 implicit relative import 寫法（Python 3 不支援）
from sample_module import sample_func
指令 1. 成功印出 Hello!
指令 2. ModuleNotFoundError。因為 Python 3 不支援 implicit relative import （前面不加點的寫法），故會將之當作 absolute import，但第三個例子才是正確寫法。

# 標準的 explicit relative import 寫法
from .sample_module import sample_func
指令 1. 包含相對路徑的檔案不能直接執行，只能作為 module 被引用，所以失敗
指令 2. 成功印出 Hello!

# 標準的 absolute import 寫法
from sample_package.sample_module import sample_func
指令 1. 如果此層目錄位置不在 python path 中，就會失敗
指令 2. 成功印出 Hello!

執行指令中的 -m是為了讓 Python 預先 import 你要的 package 或 module 給你，然後再執行 script
所以這時 sample_module_import 在跑的時候，是以 sample_package 為環境的，這樣那些 import 才會合理
另外，python path 是 Python 查找 module 時候使用的路徑，例如 standard module 所在的目錄位置
因此在第三種寫法中，Python 會因為在 python path 中找不到 sample_package.sample_module而跳出 error
你可以選擇把當前目錄加到 sys.path，也就是 Python path（初始化自環境變數PYTHONPATH），來讓 Python 搜尋得到這個 module ，但這個方法很髒很難維護，最多用來debug，其他時候強烈不建議使用
"""


"""
Absolute Import v.s. Relative Import
Python 有兩種 import 方法，absolute import 及 relative import
Absolute import 就是完整使用 module 路徑，Relative import 則是使用以當前 package 為參考的相對路徑
Relative import 的需求在於，有時候在改變專案架構的時候，裡面的 package 和 module 會拉來拉去
這時候如果這些 package 裡面使用的是relative import 的話，他們的相對關係就不會改變，也就是不需要再一一進入 module 裡更改路徑
但因為 relative import 的路徑取決於當前 package，所以在哪裡執行就會造成不一樣的結果，一不小心又要會跳出一堆 error，這時使用 absolute import 就會減少許多困擾

假設Package架構如下：
package
├── __init__.py
├── subpackage1
│   ├── __init__.py
│   ├── moduleX.py
│   └── moduleY.py
├── subpackage2
│   ├── __init__.py
│   └── moduleZ.py
└── moduleA.py

現在假設 package/subpackage1/moduleX.py 想要從其他 module 裡 import 一些東西，則使用下列語法（[A]表示 absolute import 範例；[R]表示 relative import 範例）
# Import 同一個 package 底下的 sibling module `moduleY`
[A] from package.subpackage1 import moduleY
[R] from . import moduleY
[Error] import .moduleY

# 從同一個 package 底下的 sibling module `moduleY` 中，
# import `spam` 這個 function
[A] from package.subpackage1.moduleY import spam
[R] from .moduleY import spam

# 從隔壁 package 底下的 module `moduleZ` 中，
# import `eggs` 這個 function
[A] from package.subpackage2.moduleZ import eggs
[R] from ..subpackage2.moduleZ import eggs

# Import parent package 底下的 module `moduleA`
[A] from package import moduleA
[R] from .. import moduleA 或 from ... package import moduleA

要點：
1.Relative import 裡，..代表上一層 ，多幾個.就代表多上幾層。
2.Relative import 一律採用 from ... import ...語法，即使是從 . import也要寫 from . import some_module 而非 import .some_module。原因是.some_module這個名稱在 expression 裡無法出現。Absolute import 則無限制。
"""

"""
常見 import 陷阱：
1.Circular Import（循環匯入）：
想像一個 module A在一開始要 import 另一個 module B 裡的東西，而很不巧的 module B也需要從 module A import 一些東西
但 module A還正在執行途中，自己都還沒定義好自己的 function ，於是你不讓我我不讓你，這種類似 deadlock 的情形正是常見的 Circular import
  例如：
  A.py
  from .B import B_greet_back

  def A_say_hello():
      print('A says hello!')
      B_greet_back()

  def A_greet_back():
      print('A says hello back!')

  if __name__ == '__main__':
      A_say_hello()

  B.py
  from .A import A_greet_back

  def B_say_hello():
      print('B says hello!')
      A_greet_back()
      
  def B_greet_back():
      print('B says hello back!')

  if __name__ == '__main__':
      B_say_hello()

  上述內容都一樣，只是A/B互換。B 很有禮貌想先打招呼。在與 sample_package 同目錄底下執行：
  $ python3 -m sample_package.B

  會得到錯誤訊息：
  Traceback (most recent call last):
    File "/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/runpy.py", line 193, in _run_module_as_main
   "__main__", mod_spec)
   File "/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/runpy.py", line 85, in _run_code
   exec(code, run_globals)
   File "/path/to/sample_package/B.py", line 2, in <module>
   from .A import A_greet_back
   File "/path/to/sample_package/A.py", line 1, in <module>
   from .B import B_greet_back
   File "/path/to/sample_package/B.py", line 2, in <module>
   from .A import A_greet_back
  ImportError: cannot import name 'A_greet_back'

  主要是因為 B 試圖 import A_greet_back，但途中先進到 A 執行，而因為 Python 是從頭開始一行一行執行下來的，於是在定義 A_greet_back之前會先碰到自己的 import statement，於是又進入 B，然後陷入死胡同
  解決這種circular import的方法如下：
  a.Import 整個 module 而非單一 attribute：
  把 B.py 更改成如下：
    # from .A import A_greet_back
    from . import A

    def B_say_hello():
        print('B says hello!')
        # A_greet_back()
        A.A_greet_back()
    ...

  這樣就不會發生錯誤，原本執行 from .A import A_greet_back 時被迫要從 load 進來的 Amodule object 中找出 A_greet_back 的定義，但此時這個 module object 還是空的；而更新後的 from . import A 就只會檢查 A module object 存不存在，至於 A_greet_back 存不存在等到需要執行的時候再去找就行了

  b.延遲 import：
  把 B.py 更改成如下：
    # 前面全刪
    def B_say_hello():
        from .A import A_greet_back
        print('B says hello!')
        A_greet_back()
    ...

  跟前面類似，Python 在跑到這行時才會 import A module，這時因為 B module 都已經 load 完了，所以不會有 circular import 的問題。但這個方法比較 hacky 一點，大概只能在 hackathon 中使用，否則正式專案裡看到這種難維護的 code 可能會有生命危險

  c.好好釐清架構，避免circular import：
  治本方法還是好好思考自己寫的 code 為什麼會陷入這種危機，然後重新 refactor 吧


2. Relative Import above Top-level Package：
  還不熟悉 relative import 的人常常會見到這個 error：
  ValueError: attempted relative import beyond top-level package

  讓我們重現一下這個 error。把 B.py 前頭更改成如下：
  # from . import A
  from ..sample_package import A

  ...

  現在我們的路徑位置在與 sample_package 同目錄底下，跑：
  $ python3 -m sample_package.B

  會得到以下錯誤：
  Traceback (most recent call last):
  File "/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/runpy.py", line 193, in _run_module_as_main
  "__main__", mod_spec)
  File "/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/runpy.py", line 85, in _run_code
  exec(code, run_globals)
  File "/path/to/sample_package/B.py", line 5, in <module>
  from ..sample_package import A
  ValueError: attempted relative import beyond top-level package

  所謂的 top-level package 就是你所執行的 package 中最高的那一層，也就是 sample_package。超過這一層的 relative import 是不被允許的，指的就是..sample_package 這行嘗試跳一層上去而超過 sample_package了
  可以試試更改當前目錄到上一層（cd ..），假設叫 parent_folder ，然後執行 python3 -m parent_folder.sample_package.B，就會發現 error 消失了，因為現在的 top-level package 已經變成 parent_folder了

  Import 是各大語言必備功能，看似簡單，使用上來說陷阱卻頗多。如果搞不清楚 Python 中的 import 是怎麼運作的，除了在整體專案架構上難以靈活設計，更可能要陷入可怕的 error 海了
  """
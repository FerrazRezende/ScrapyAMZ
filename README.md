<h6 align="center"><b>Welcome, this is my first public project in GitHub!!

ScrapyAMZ is a script for scraping for 10.000 data in department "Computers". In dataset contains: Price, Anouncement title, Ratings, Notes and link for product.

 I hope this content anything help you</h6></b>


<h1 align="center">ScrapyAMZ</h1>
<br>

- Install and setting script
- Execute script
- Clarifications
- Final considerations

<br>

<h1>Install and configuration script settings:</h1>
<p>First step is cloning the repository

After in any project in python is create the virtual enviroment 
</p>



<p>
In command prompt in project dir, digit:
</p>

``` python
python -m venv venv
```

<p>This command create a directory named venv, we will storage the dependences here. For this, activate the venv:

in windows:</p>

```
source venv/Scripts/activate
```

<p> 
in mac or linux:
</p>

```
source venv/bin/activate
```

<p>The console should look like this:</p>
<img src="https://i.ibb.co/jGMbzy5/Sem-t-tulo.png" alt="venv-activated" border="0">

<p>
With venv enabled, installing the dependencies in file "requirements.txt"
</p>

```
pip install -r requirements.txt
```

<p>Check if all dependencies is installed:<p>

```
pip freeze
```

<p>The result should be:</p>
<img src="https://i.ibb.co/S55jwVD/2.png" alt="2" border="0">

<h3>Now, is all right to execute script... but, before is need configure settings to send e-mail. </h3>

<p>Due to recent changes in Google's treatment of third-party app usage, additional settings are required to sending e-mails.</p>
<a href="https://support.google.com/accounts/answer/3466521?hl=pt-BR">To see more about Google's policy change, click here</a>
<br>
<h3>Settings e-mail: </h3>
<p>Access the file "SendEmail.py"</p>
<img src="https://i.ibb.co/nQjt0dV/3.png" alt="3" border="0">

<img src="https://i.ibb.co/4Zd2rpg/4.png" alt="4" border="0">

<h3>1 - Setting sender e-mail</h3>

<h3>2 - Access <a href="google.com">Google.com</a> and go to 'Manage you Google account' </h3>
<img src="https://i.ibb.co/MPmVJqH/5.png" alt="5" border="0">

<h3> Go to section 'Security' </h3>
<img src="https://i.ibb.co/vVKdPY6/10.png" alt="10" border="0">

<h3>For this step, you need to have activate 2-Step activation.</h3> 
<img src="https://i.ibb.co/DCgMX66/11.png" alt="11" border="0">

<h3>Next, go to apps passwords, enter you account passwor </h3>
<h4>Select app 'Mail'</h4>
<img src="https://i.ibb.co/cLWj37P/12.png" alt="12" border="0">

<h4>Select 'other device' to setting a name for password </h4>
<img src="https://i.ibb.co/Kynj8Zk/133.png" alt="133" border="0">
<img src="https://i.ibb.co/sv4p4tS/14.png" alt="14" border="0">

<p>After complete all steps, the site return a password (don't worry, this key not giving access to your account, it is possible to delete any key you own at any time.</p>

<img src="https://i.ibb.co/26wRZps/15.png" alt="15" border="0">

<h4> For finish, insert a key generated in 'password':</h4>
<img src="https://i.ibb.co/8BTgVT2/6.png" alt="6" border="0">

<h1>Executing script:</h1>
<p>With a venv activate, digit: </p>

```
python main.py
```

<p>The script request 2 inputs: File format (CSV or Json) and E-mail to recive the file</p>
<img src="https://i.ibb.co/Tqtv1SY/7.png" alt="7" border="0">

<p>The script collect the dataset:</p>

- Price
- Anounce title
- Ratings
- Notes
- Link to anounce 

<h1>Clarifications:</h1>

<h3>Regex:</h3>
<p>I used a validation template for the email through re, however I had a problem when sending to email's with 
the following template xxxxx.xxxxx.xxx@gmail.com, I also saw no need to fix it, instead
the script scraps and saves the data locally before checking the email validation, so if the email
is invalid, the file will still be saved in the ./output folder.</p>

Template re:
```
'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' # It is up to you to correct or not =)
```
<br>
<h3>Erro timeout 504 Urrlib:</h3>
<p>During the development process, when scraping several pages, between pages 67 and 75 the script
script was interrupted due to a connection problem with the site's server:</p>
<img src="https://i.ibb.co/x6Vrtt1/17.png" alt="17" border="0">

<p>I fixed this by using a while loop that will keep repeating the access to the site until the response to the request is 200 </p>

``` python
while True:
    try:
        req = Request('https://sp.olx.com.br/sao-paulo-e-regiao/imoveis/aluguel?o={}'.format(i), headers=hdrs)
        response = urlopen(req)
        self.html = response.read()
        if response.getcode() == 200:
            break
        except Exception as inst:
            print(inst)
```

<img src="https://i.ibb.co/4VzLPdM/9.png" alt="9" border="0">

<br>
<h3>Amazon Site Page Limit:</h3>
<p>When I was looking for public data to do a big data collection, I was surprised by the amount of 
data available on Amazon... However, during development I noticed that Amazon limits it to
400 visible pages and so I manually entered the number into the "pages" variable (remembering that the count always starts from 0).</p>
<img src="https://i.ibb.co/pfSWVc4/10.png" alt="10" border="0">

<h1>Final considerations</h1>
<h3>I hope this script can help you in some way and that it is of good use!</h3><br> 



<p>There are many uses for data scraping and several other ways to do it, feel free
to update the content and make the changes you think necessary. Study is never too much!</p>

<p>If you have any questions, feel free to contact us, <a href="https://wa.me/5511980448707">Whatsapp</a>
or <a href="https://discordapp.com/users/Matheus-Ferraz#3474">Discord</a></p>


<h2>I work freelance scraping data </h2>
<p>If you need a specific data scraping, which even requires login to access the data,
contact-me <a href="https://wa.me/5511980448707"></a></p>
<p></b>Table of values:</b></p>
        <p>1 a 5.000 datasets: $ 5,00</p>
        <p>5.000 a 15.000 datasets: $ 10,00</p>
        <p>15.000 a 50.000 datasets: $ 25,00</p>
        <p>50.000 a 150.000 datasets: $ 50,00</p>
        <p>150.000 a 300.000 datasets: $ 100,00</p>
        <p>for more information, contact me</p>
<h1 align="center">Thanks for getting this far, good studies!!!!</h1>

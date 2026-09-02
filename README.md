# Front-end with Streamlit

> **If you have not finished yesterday's mandatory challenge, finish those first: challenges 1 and 2. Then come back here.**

## 🎯 Objectives

So far we made an API, which is already a big step: it means anyone who knows how to use an API can get predictions from our model, without knowing anything about the code to do that. They don't even need to master Python. Developers coding in other languages like JavaScript, Ruby, or Java could use our API. 💪

But the API is not very friendly towards end users: it's still a programming interface. How can we make it more accessible?

Let's create our own website ! 🔥

We are going to use **Streamlit** which will allow us to create a website very easily and without any web development skills.


## 1) First, let's create another website project ⚙️


### 1.1) Create a new repo

You will create a new project repository for the code of our website. (Want to know why? Keep reading.)

Again, this directory will be located inside your *projects directory*: `~/code/<user.github_nickname>`.

👉 Create a new project named `zoologist-front`.

```bash
cd ~/code/<user.github_nickname>
uv init --python 3.12.9 zoologist-front
cd zoologist-front
uv sync
code .
```

Open a terminal inside VS Code. Stick to this one: it's always easier to use your IDE's terminal (IDE = Integrated Development Environment; VS Code for us.).

👉 Create a corresponding repository on your **GitHub** account:

``` bash
gh repo create zoologist-front --private --source=. --remote=origin
```

👉 Go to the GitHub repo to make sure that everything is ok:

``` bash
gh browse
```

The repository is empty, which is normal since you haven't pushed any code yet...

The GitHub page shows some instructions to get started, but you can ignore these. You already created and linked your local repo.

We are now all set!

### 1.2) Set up the structure

👉 Delete the `main.py` file. We don't need it.

👉 Open the `README.md` and add a description for your project:

```markdown
# The Zoologist Front-end

A Streamlit app to expose the Zoologist penguin classification model to end users.

Uses the [Zoologist project](https://www.github.com/<user.github_nickname>/zoologist) as back-end.
```

👉 Open `pyproject.toml` and update the description:

```markdown
A Streamlit front-end for the Zoologist project
```

### 1.3) Create a new python virtual environment

For the website, you will create **a new python virtual environment**.

#### 1.3.1. Why?

<details>
<summary markdown='span'>❓Think about it, and then click to read the answer.</summary>

**In the previous unit, you created an API** for the zoologist model. This API can be used by anyone. You used it from the browser for example, without any code. So, to use the API, we don't need data science libraries like scikit-learn anymore. Scikit-learn is used **inside** the API, but **outside** users don't need it. That's why you created an API in the first place...

In this unit, **we are creating a website**. You will be doing that using Python, because by now you are pretty comfortable using this little 🐍. If our product is succesful, we will ask web developers to create a fancy front-end for us. And they might do that in Python, or in Ruby or JavaScript, whatever they like. One thing is sure: they are not data scientists, and won't work with our data science packages.

**Long story short: we don't need our data science packages for our website.**

These are the same reasons we create a separate repository for the front-end: website creators don't need to know the back-end code. They just need to know how the API works.

By using a separate repo, we can also keep our modeling code secret (if we use a private repo on GitHub): maybe we want to share the API, but we don't want to give away all our proprietary code.

</details>

#### 1.3.2. Let's create the Python environment

Follow the same procedure you used to create the environment for the `zoologist` project.

First, you initiate the project:
   - You already did that with `uv init` in the previous step.
   - That created the essential `pyproject.toml`.
   - When we ran `uv sync`, it reated the virtual environment.

Next you need to add the dependencies. Think a minute about what you will need.

<details>
<summary markdown='span'>So, what do you need❓</summary>

Well, it turns out you don't need anything but `streamlit`!

As we said before, we don't need any data science packages. We just need to be able to launch `streamlit`, and to make requests to our API.

To make requests, we need the `requests` package, but `streamlit` will already install that for us.

</details>

👉 Let's add our main dependency, Streamlit:

   - Run `uv add streamlit`.
   - You'll see it installing a bunch of packages (blazingly fast, that's the advantage of `uv`).
   - Check `pyproject.toml` and how the dependencies where changed.
   - Have a look at `uv.lock`. This is where `uv` lists all the specific packages it installed following `uv add streamlit`. Never edit this file by hand! Only change `pyproject.toml`, or even safer, use `uv add` and `uv remote`.
   - See that `uv` created the `.venv` folder for you: it contains all the installed dependencies of your project.
   - Check the installed packages with `uv pip freeze` or `uv pip list`. You might have to run `pyenv deactivate` first (otherwise it will list the packages from the `lewagon` environment).

What is included with Streamlit? A lot. The main ones we care about are:

   - `altair`: a data viz package; we haven't explored it yet, but it's the one Streamlit uses under the hood when you create Streamlit charts.
   - `numpy` and `pandas`: handy, we don't need to install them; be aware that the versions might be different from what you're used to.
   - `pillow`: a library to work with images (`import PIL`).
   - `requests`: to make API requests; we used it at the start of the bootcamp in the _Data Sourcing_ unit.


#### 1.3.3. Use the virtual environment

That was all you needed to set up this _in-project_ virtual environment.

As long as you are inside your project folder structure, you just need to write `uv run <command>` to use the local environment.

### 1.4) Initial commit of our project setup

👉 Check which files are ready to be staged:

```bash
git status
```

There should be four.

👉 Now `git add` them. Preferably by listing the files explicitly. If you ran `git add .`, make sure you run `git status` to check which files are staged to avoid nasty surprises.

👉  Then commit and push:

```bash
git commit -m "initial commit"
```

```bash
git push
```

👉 Use `gh browse` to check your repo online. Do you see the same files? You should.


## 2) Create a streamlit website

Let's get working for real now. First create a new branch `simple-app`.

### 2.1) File structure

First, we need an `app.py` file inside of our project. This file will contain the code for our page. Any other name would also work, but `app` sounds right.

We have created some boilerplate code for you, copy it inside your project:

``` bash
```bash
cp ~/code/<user.github_nickname>/{{ local_path_to("07-Intro-to-ML-Ops/03-Front-end-and-data-in-the-cloud/01-Streamlit") }}/app.py ~/code/<user.github_nickname>/zoologist-front/
```

Your project should look like this now:

``` bash
.
├── .venv
├── .gitignore
├── .python-version
├── app.py
├── pyproject.toml
├── README.md
└── uv.lock
```

Not too overwhelming, right ? 😉

Well ... this is half the work.

### 2.2) Launch the minimal website

👉 Let's have a look at the code inside `app.py`:

1. It starts with `import streamlit`. The convention is to name it `st`.

2. Then we see a lot of multiline strings, and the use of `st.markdown()`.

👉 Let's run the **Streamlit** web server and see what the website looks like. In the documentation you will see to simply run `streamlit run your_file.py`. Since we are using `uv`, we have to prepend it with `uv run`, just like when we run `python`:

``` bash
uv run streamlit run app.py
```

This usually will open your browser. Check the url it uses. Which port does it use?

You have a website running on your machine 🎉

### 2.3) Now you need to plug the API into the website

... So that users can actually make some predictions!

In the next steps you will follow the instructions inside the web page and replace the content with some `requests` package magic and a call to the API!

Make sure your API is running. But which one should you use? We have three options:

- Locally, running `uvicorn` straight into our terminal.
- Locally, using the local Docker image with `docker run`.
- The version deployed on the cloud.

In this case we know that we have a functioning API in the cloud. So probably everything will work, but we're not sure: maybe things will be different now that you use the API from the Streamlit app.

That's why while developing you better use the version that will be the easiest to debug: the local one, running in your local environment. Once everything works, you can switch to the one running on the cloud, and hopefully everything will still work. 🤞

In this challenge, stick to your local API. When we deploy to the cloud, we'll switch to the API in the cloud.

### 2.4) Creating the controls and connecting to the API.

**Read this whole section before you get started!**

Once your API is running, start coding in `app.py` following the instructions inside. Gradually replace the multi-line strings with actual code. Do this step-by-step. Everytime you make a change, check the result in your browser.

You don't need to restart Streamlit to see the results:

- In the top right corner, click on the 3 dots for the menu, and hit _Rerun_.
- Or better: set it up to reload automaticallly whenever you save your `app.py` file: in the menu go to _Settings_ and select _Run on save_.

To know how to add controls and outputs to your page, either check the Streamlit documentation, or have a look at [https://streamlit.lewagon.ai/](https://streamlit.lewagon.ai/) where we made a Streamlit site with examples of the most common controls.

For this first rendition of your site, keep it simple and minimal: at this stage we don't want it to be beautiful, we want to have a first working version. Later, when you have time, you can still improve the styling. This is another example of incremental steps to break down complexity.

Regularly commit your changes! It is very easy to accidentally mess up everything. So every time you made a change that works, commit it.

Examples of when you want to commit:
- When you made the code for the controls
- When you made the code for the API request
- When you made the code to display the result
- ...

👉 Now open `app.py` and start coding.

## 3) Finishing up

Make sure you committed all your changes, then push your code.

## 4) Run the tests

👉 Go back to the terminal window where you opened this challenge. If you closed it, open a new terminal (outside VS Code), and run the first line from the terminal instructions at the top of this challenge.

👉 Then run the tests for this part:

```bash
pytest
```

If all tests passed (you get a green result), it's time to send your accomplishments to Kitt.

👉 Run the commands below.

```bash
make test
git add tests/test_output.txt
git commit -m "Streamlit created"
git push origin master
```

At this point, your status on Kitt should be green. If not, check with a TA.


## 🏁 Wrapping it up

You made a (rudimentary) front-end for our model.

Main takeaways:
- You do this in a separate repo, with a dedicated virtual environment. Creating a front-end is another business than making a machine learning API. We want to separate both.
- You used Streamlit. It is great because it allows data scientists to **quickly** make a functional front-end in their favourite language - Python - and it comes with lots of data-related bells and whistles.
- Because of this, Streamlit is great to showcase what an end product could look like to management, investors, ...
- Once you are past this *"proof of concept"* (POC) phase, you might consider hiring a team of web devs to make a really beautiful website.

🏁 Congratulations! You have created a working Streamlit site locally. In the next challenge, we'll expose it to the outside world.

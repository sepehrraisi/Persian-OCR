<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/sepehrraisi/Persian-OCR">
    <img src="README/images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Persian-OCR</h3>

  <p align="center">
    A project to bring high accuracy OCR to Persian language!
    <br />
    <a href="https://github.com/sepehrraisi/Persian-OCR"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a> -->
    <!-- · -->
    <!-- <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a> -->
    <!-- · -->
    <!-- <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a> -->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>

[//]: # (    <li><a href="#contributing">Contributing</a></li>)

[//]: # (    <li><a href="#license">License</a></li>)

[//]: # (    <li><a href="#contact">Contact</a></li>)

[//]: # (    <li><a href="#acknowledgments">Acknowledgments</a></li>)
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[//]: # (<a  align="center" href="https://github.com/sepehrraisi/Persian-OCR">)

[//]: # (    <img src="README/images/screenshot.png" alt="ScreenShot">)

[//]: # (</a>)

As I was looking for a good Persian OCR, I've found out that there is no good open-source project that features Persian language for OCR.
So I've started a project to create a simple Persian OCR to achieve the missing.
 
What I have Done:
* Optimize pytesseract for persian by testing different configs.
* Image Optimization for low-res images to improve accuracy significantly.
* Using a Persian Spell-Checking to improve accuracy.

Of course, This project isn't perfect and i'm still working on it to improve accuracy and speed. But I hope this project helps other people like me to have a good base for Persian OCR.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

I have used python to build this project.
Two of the most useful modules in this project were pytesseract and opencv.

[//]: # (* [![Next][Next.js]][Next-url])

[//]: # (* [![React][React.js]][React-url])

[//]: # (* [![Vue][Vue.js]][Vue-url])

[//]: # (* [![Angular][Angular.io]][Angular-url])

[//]: # (* [![Svelte][Svelte.dev]][Svelte-url])

[//]: # (* [![Laravel][Laravel.com]][Laravel-url])

[//]: # (* [![Bootstrap][Bootstrap.com]][Bootstrap-url])

[//]: # (* [![JQuery][JQuery.com]][JQuery-url])

[//]: # (<p align="right">&#40;<a href="#readme-top">back to top</a>&#41;</p>)



<!-- GETTING STARTED -->
## Getting Started

This is a simple instruction to start using this project.

### Prerequisites

You need to install pytesseract on your device:
* Ubuntu
  ```sh
   sudo apt-get install tesseract-ocr
  ```
You need to add Persian Language to tesseract:
* Ubuntu
  ```sh
   sudo apt-get install tesseract-ocr-fas
  ```

### Installation

Now that you've installed tesseract we can move on with Persian-OCR:_

1. Clone the repo
   ```sh
   git clone https://github.com/sepehrraisi/Persian-OCR && \
   cd Persian-OCR
   ```
2. Create a Virtual Environment for python and Source it:
   ```sh
   python3 -m venv venv && \
   source ./venv/bin/activate
   ```
3. Install Python modules `requirements.txt`
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

After installing the requirements you can use it by running the `ocr.py` file:
```sh
python ./ocr.py -i <inputfile> -o <outputfile>     
```
Then it will write the results to `outputfile`

[//]: # (_For more examples, please refer to the [Documentation]&#40;https://example.com&#41;_)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Use pytesseract to extract text
- [x] Improve accuracy by simple opencv features
- [ ] Improve accuracy by UpScaling the images
- [ ] Add modular capabilities to improve functionality
- [ ] Add Table recognition
- [x] Multi-language Support
    - [x] Persian
    - [x] English

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



[//]: # (<!-- CONTRIBUTING -->)

[//]: # (## Contributing)

[//]: # ()
[//]: # (Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.)

[//]: # ()
[//]: # (If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".)

[//]: # (Don't forget to give the project a star! Thanks again!)

[//]: # ()
[//]: # (1. Fork the Project)

[//]: # (2. Create your Feature Branch &#40;`git checkout -b feature/AmazingFeature`&#41;)

[//]: # (3. Commit your Changes &#40;`git commit -m 'Add some AmazingFeature'`&#41;)

[//]: # (4. Push to the Branch &#40;`git push origin feature/AmazingFeature`&#41;)

[//]: # (5. Open a Pull Request)

[//]: # ()
[//]: # (<p align="right">&#40;<a href="#readme-top">back to top</a>&#41;</p>)

[//]: # ()
[//]: # ()
[//]: # ()
[//]: # (<!-- LICENSE -->)

[//]: # (## License)

[//]: # ()
[//]: # (Distributed under the MIT License. See `LICENSE.txt` for more information.)

[//]: # ()
[//]: # (<p align="right">&#40;<a href="#readme-top">back to top</a>&#41;</p>)

[//]: # ()
[//]: # ()
[//]: # ()
[//]: # (<!-- CONTACT -->)

[//]: # (## Contact)

[//]: # ()
[//]: # (Your Name - [@your_twitter]&#40;https://twitter.com/your_username&#41; - email@example.com)

[//]: # ()
[//]: # (Project Link: [https://github.com/your_username/repo_name]&#40;https://github.com/your_username/repo_name&#41;)

[//]: # ()
[//]: # (<p align="right">&#40;<a href="#readme-top">back to top</a>&#41;</p>)

[//]: # ()
[//]: # ()
[//]: # ()
[//]: # (<!-- ACKNOWLEDGMENTS -->)

[//]: # (## Acknowledgments)

[//]: # ()
[//]: # (Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!)

[//]: # ()
[//]: # (* [Choose an Open Source License]&#40;https://choosealicense.com&#41;)

[//]: # (* [GitHub Emoji Cheat Sheet]&#40;https://www.webpagefx.com/tools/emoji-cheat-sheet&#41;)

[//]: # (* [Malven's Flexbox Cheatsheet]&#40;https://flexbox.malven.co/&#41;)

[//]: # (* [Malven's Grid Cheatsheet]&#40;https://grid.malven.co/&#41;)

[//]: # (* [Img Shields]&#40;https://shields.io&#41;)

[//]: # (* [GitHub Pages]&#40;https://pages.github.com&#41;)

[//]: # (* [Font Awesome]&#40;https://fontawesome.com&#41;)

[//]: # (* [React Icons]&#40;https://react-icons.github.io/react-icons/search&#41;)

[//]: # ()
[//]: # (<p align="right">&#40;<a href="#readme-top">back to top</a>&#41;</p>)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/sepehrraisi/Persian-OCR.svg?style=for-the-badge
[contributors-url]: https://github.com/sepehrraisi/Persian-OCR/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/sepehrraisi/Persian-OCR.svg?style=for-the-badge
[forks-url]: https://github.com/sepehrraisi/Persian-OCR/network/members
[stars-shield]: https://img.shields.io/github/stars/sepehrraisi/Persian-OCR.svg?style=for-the-badge
[stars-url]: https://github.com/sepehrraisi/Persian-OCR/stargazers
[issues-shield]: https://img.shields.io/github/issues/sepehrraisi/Persian-OCR.svg?style=for-the-badge
[issues-url]: https://github.com/sepehrraisi/Persian-OCR/issues
[license-shield]: https://img.shields.io/github/license/sepehrraisi/Persian-OCR?style=for-the-badge
[license-url]: https://github.com/sepehrraisi/Persian-OCR/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/sepehrraisi
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 

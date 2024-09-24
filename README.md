<style>
  .morning-animation {
    width: 50px;
    height: 50px;
    background: yellow;
    border-radius: 50%;
    box-shadow: 0 0 20px rgba(255, 215, 0, 0.7);
    animation: sun-rise 3s ease-in-out infinite alternate;
  }

  .afternoon-animation {
    width: 50px;
    height: 50px;
    background: orange;
    border-radius: 50%;
    box-shadow: 0 0 15px rgba(255, 165, 0, 0.7);
    animation: sun-glow 3s ease-in-out infinite alternate;
  }

  .evening-animation {
    width: 50px;
    height: 50px;
    background: red;
    border-radius: 50%;
    box-shadow: 0 0 10px rgba(255, 69, 0, 0.7);
    animation: sunset-fade 3s ease-in-out infinite alternate;
  }

  .night-animation {
    width: 50px;
    height: 50px;
    background: darkblue;
    border-radius: 50%;
    position: relative;
    animation: moon-glow 4s ease-in-out infinite alternate;
  }

  .night-animation::before {
    content: "";
    position: absolute;
    top: 10px;
    left: 10px;
    width: 20px;
    height: 20px;
    background: lightgray;
    border-radius: 50%;
  }

  /* Animations */
  @keyframes sun-rise {
    from {
      transform: translateY(10px);
    }
    to {
      transform: translateY(-10px);
    }
  }

  @keyframes sun-glow {
    from {
      transform: scale(1);
      box-shadow: 0 0 20px rgba(255, 165, 0, 0.5);
    }
    to {
      transform: scale(1.2);
      box-shadow: 0 0 30px rgba(255, 165, 0, 0.9);
    }
  }

  @keyframes sunset-fade {
    from {
      opacity: 1;
      transform: translateY(0);
    }
    to {
      opacity: 0.7;
      transform: translateY(5px);
    }
  }

  @keyframes moon-glow {
    from {
      transform: scale(1);
      box-shadow: 0 0 20px rgba(173, 216, 230, 0.7);
    }
    to {
      transform: scale(1.1);
      box-shadow: 0 0 30px rgba(173, 216, 230, 1);
    }
  }
</style>

<script>
  function getGreeting() {
    const currentHour = new Date().getHours();
    let greeting;

    if (currentHour >= 5 && currentHour < 12) {
      greeting = `<span>Good Morning</span> <div class="morning-animation"></div>`;
    } else if (currentHour >= 12 && currentHour < 17) {
      greeting = `<span>Good Afternoon</span> <div class="afternoon-animation"></div>`;
    } else if (currentHour >= 17 && currentHour < 21) {
      greeting = `<span>Good Evening</span> <div class="evening-animation"></div>`;
    } else {
      greeting = `<span>Good Night</span> <div class="night-animation"></div>`;
    }

    document.getElementById('greeting').innerHTML = greeting;
  }

  getGreeting();
</script>

<h1 id="greeting"></h1>


<p></p>
<h2>🚀 Languages and Tools I Use</h2>
<p>
    <span style="pointer-events: none;">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/c/c-original.svg" alt="c" title="c" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg" alt="cplusplus" title="cplusplus" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/csharp/csharp-original.svg" alt="csharp" title="csharp" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg" alt="java" title="java" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" title="javascript" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/typescript/typescript-original.svg" alt="typescript" title="typescript" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/php/php-original.svg" alt="php" title="php" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vuejs/vuejs-original-wordmark.svg" alt="vuejs" title="vuejs" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" title="react" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/angularjs/angularjs-original-wordmark.svg" alt="angularjs" title="angularjs" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://angular.io/assets/images/logos/angular/angular.svg" alt="angular" title="angular" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" title="bootstrap" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" title="css3" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" title="html5" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/redux/redux-original.svg" alt="redux" title="redux" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://www.vectorlogo.zone/logos/flutterio/flutterio-icon.svg" alt="flutter" title="flutter" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://www.vectorlogo.zone/logos/dartlang/dartlang-icon.svg" alt="dart" title="dart" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" title="mysql" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://www.svgrepo.com/show/303229/microsoft-sql-server-logo.svg" alt="mssql" title="mssql" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://www.chartjs.org/media/logo-title.svg" alt="chartjs" title="chartjs" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/dot-net/dot-net-original-wordmark.svg" alt="dotnet" title="dotnet" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/photoshop/photoshop-line.svg" alt="photoshop" title="photoshop" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://www.vectorlogo.zone/logos/figma/figma-icon.svg" alt="figma" title="figma" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" title="postman" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://cdn.worldvectorlogo.com/logos/nextjs-2.svg" alt="nextjs" title="nextjs" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://www.vectorlogo.zone/logos/gatsbyjs/gatsbyjs-icon.svg" alt="gatsby" title="gatsby" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" title="git" width="42" height="42" />
    </span>
    <span style="pointer-events: none;">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" title="linux" width="42" height="42" />
    </span>
</p>

<h2>⚡️ Where to find me</h2>
<p>
  <a target="_blank" href="https://www.linkedin.com/in/bbus24/" style="display: inline-block;">
    <img src="https://img.shields.io/badge/linkedin-logo?style=for-the-badge&logo=linkedin&logoColor=white&color=#0a77b6" alt="linkedin" />
  </a>
</p>

<div align="center">
  <span style="pointer-events: none;">
    <img src="https://github-readme-stats.vercel.app/api?username=Bibash-24&show_icons=true&locale=en" height="150" alt="stats graph" title="GitHub Stats" />
  </span>
  <span style="pointer-events: none;">
    <img src="https://github-readme-stats.vercel.app/api/top-langs?username=Bibash-24&show_icons=true&locale=en&layout=compact" height="150" alt="languages graph" title="Top Languages" />
  </span>
</div>

<div align="center">
  <span style="pointer-events: none;">
    <img src="https://github-readme-streak-stats.herokuapp.com/?user=Bibash-24&" alt="contribution graph" title="Contribution Streak" />
  </span>
  <span style="pointer-events: none;">
    <img src="https://github-profile-trophy.vercel.app/?username=Bibash-24" alt="trophies" title="Trophies" />
  </span>
</div>

const gitImagePath = require("git-img-path");

gitImagePath
  .gitImages("ms2pony", "ms2pony.github.io", "source\\_posts\\img")
  .then((fileResult) => {
    console.log(fileResult);
  });

const { readFileSync } = require("fs");
const gitImagePath = require("git-img-path");
const markdownLinkExtractor = require("markdown-link-extractor");

gitImagePath
  .gitImages("ms2pony", "ms2pony.github.io", "source\\_posts\\img")
  .then((fileResult) => {
    console.log(fileResult.image20220202234522365png);
  });

const markdown = readFileSync("source/_posts/t1.md", { encoding: "utf8" });

// const links = markdownLinkExtractor(markdown, false);
// links.forEach((link) => console.log(link));

const details = markdownLinkExtractor(markdown, true);
details.forEach((detail) => console.log(detail.raw));

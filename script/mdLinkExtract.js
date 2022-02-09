/**
 * 抽取指定文件中的链接
 */
const { readFileSync } = require("fs");
const markdownLinkExtractor = require("markdown-link-extractor");

workfile = process.env.WORKPATH + "\\windows.md";
const markdown = readFileSync(workfile, { encoding: "utf8" });

// const links = markdownLinkExtractor(markdown, false);
// links.forEach((link) => console.log(link));

const details = markdownLinkExtractor(markdown, true);
const imgDetails = new Array();
details.forEach((detail) => {
  if (detail.type == "image") {
    // console.log(detail);
    imgDetails.push(detail);
  }
});
data = JSON.stringify(imgDetails);
console.log(data);

"use strict";
const studio = document.querySelector(".studio");
const demoButtons = Array.from(document.querySelectorAll("[data-demo]"));
const copy = JSON.parse(document.getElementById("demo-copy").textContent);
function setDemo(clean) {
  studio.classList.toggle("clean", clean);
  demoButtons.forEach(function (button) {
    button.setAttribute("aria-pressed", String(button.dataset.demo === (clean ? "after" : "before")));
  });
  document.getElementById("demo-state").textContent = clean ? copy.afterState : copy.beforeState;
  document.getElementById("demo-result").textContent = clean ? copy.afterResult : copy.beforeResult;
}
demoButtons.forEach(function (button) {
  button.addEventListener("click", function () { setDemo(button.dataset.demo === "after"); });
});
document.querySelectorAll("[data-show-demo]").forEach(function (link) {
  link.addEventListener("click", function () { setDemo(true); });
});
const ns = "http://www.w3.org/2000/svg";
const waveform = document.getElementById("wave-bars");
for (let i = 0; i < 215; i++) {
  const rect = document.createElementNS(ns, "rect");
  const height = 8 + ((i * 37 + i * i * 7) % 31);
  rect.setAttribute("x", String(i * 5));
  rect.setAttribute("y", String((43 - height) / 2));
  rect.setAttribute("width", "2.8");
  rect.setAttribute("height", String(height));
  rect.setAttribute("rx", "1.1");
  rect.setAttribute("fill", "#a7ad9b");
  waveform.appendChild(rect);
}
const galleryCopy = JSON.parse(document.getElementById("gallery-copy").textContent);
const galleryButtons = Array.from(document.querySelectorAll("[data-gallery]"));
const galleryImage = document.getElementById("product-screenshot");
const galleryTitle = document.getElementById("gallery-title");
const galleryDescription = document.getElementById("gallery-description");
const lightbox = document.getElementById("screenshot-dialog");
const lightboxImage = document.getElementById("lightbox-image");
const lightboxTitle = document.getElementById("lightbox-title");
function setGallery(index, focus) {
  const data = galleryCopy[index];
  galleryButtons.forEach(function (button, n) {
    button.setAttribute("aria-selected", String(n === index));
    button.tabIndex = n === index ? 0 : -1;
  });
  galleryImage.src = data.image;
  galleryImage.alt = data.alt;
  document.getElementById("gallery-panel").setAttribute("aria-labelledby", "gallery-tab-" + index);
  galleryTitle.textContent = data.title;
  galleryDescription.textContent = data.description;
  lightboxImage.src = data.image;
  lightboxImage.alt = data.alt;
  lightboxTitle.textContent = data.label;
  if (focus) galleryButtons[index].focus();
}
galleryButtons.forEach(function (button, index) {
  button.addEventListener("click", function () { setGallery(index, false); });
  button.addEventListener("keydown", function (event) {
    let next;
    if (event.key === "ArrowRight") next = (index + 1) % galleryButtons.length;
    if (event.key === "ArrowLeft") next = (index + galleryButtons.length - 1) % galleryButtons.length;
    if (event.key === "Home") next = 0;
    if (event.key === "End") next = galleryButtons.length - 1;
    if (next !== undefined) { event.preventDefault(); setGallery(next, true); }
  });
});
document.querySelector(".screen-frame").addEventListener("click", function () {
  lightbox.showModal();
});
document.querySelector(".lightbox-close").addEventListener("click", function () { lightbox.close(); });
lightbox.addEventListener("click", function (event) { if (event.target === lightbox) lightbox.close(); });
const menuToggle = document.querySelector(".menu-toggle");
const nav = document.getElementById("main-nav");
menuToggle.addEventListener("click", function () {
  const open = menuToggle.getAttribute("aria-expanded") !== "true";
  menuToggle.setAttribute("aria-expanded", String(open));
  nav.classList.toggle("open", open);
});
nav.querySelectorAll("a").forEach(function (link) {
  link.addEventListener("click", function () {
    menuToggle.setAttribute("aria-expanded", "false");
    nav.classList.remove("open");
  });
});
let announceTimer;
function announce(message) {
  const region = document.getElementById("announcement");
  region.textContent = message;
  clearTimeout(announceTimer);
  announceTimer = setTimeout(function () { region.textContent = ""; }, 2600);
}
document.querySelector(".copy-button").addEventListener("click", async function () {
  try {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText("brew install ffmpeg");
    } else {
      const selection = window.getSelection();
      const range = document.createRange();
      range.selectNodeContents(document.getElementById("install-command"));
      selection.removeAllRanges();
      selection.addRange(range);
      if (!document.execCommand("copy")) { announce(copy.selectCommand); return; }
      selection.removeAllRanges();
    }
    announce(copy.copied);
  } catch (_) { announce(copy.selectCommand); }
});

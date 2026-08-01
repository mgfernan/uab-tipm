(function () {
  var indicatorId = "slide-path-indicator";

  function getSlideLevel(slide) {
    if (!slide || !slide.className) {
      return null;
    }

    var match = slide.className.match(/\blevel(\d+)\b/);
    return match ? Number(match[1]) : null;
  }

  function getSlideTitle(slide) {
    if (!slide) {
      return "";
    }

    var heading = slide.querySelector("h1, h2, h3, h4, h5, h6");
    return heading ? heading.textContent.trim() : "";
  }

  function computeParentPaths() {
    if (!window.Reveal || typeof window.Reveal.getSlides !== "function") {
      return new Map();
    }

    var slides = window.Reveal.getSlides();
    var knownTitlesByLevel = [];
    var parentPathsBySlide = new Map();

    slides.forEach(function (slide) {
      var level = getSlideLevel(slide);

      if (!level) {
        var fallback = knownTitlesByLevel.filter(Boolean);
        parentPathsBySlide.set(slide, fallback);
        return;
      }

      var parentPath = [];
      for (var i = 1; i < level; i += 1) {
        if (knownTitlesByLevel[i]) {
          parentPath.push(knownTitlesByLevel[i]);
        }
      }
      parentPathsBySlide.set(slide, parentPath);

      var title = getSlideTitle(slide);
      if (title) {
        knownTitlesByLevel[level] = title;
      }

      for (var j = level + 1; j < knownTitlesByLevel.length; j += 1) {
        knownTitlesByLevel[j] = undefined;
      }
    });

    return parentPathsBySlide;
  }

  function ensureIndicatorNode() {
    var existing = document.getElementById(indicatorId);
    if (existing) {
      return existing;
    }

    var node = document.createElement("div");
    node.id = indicatorId;
    node.setAttribute("aria-live", "polite");

    var revealRoot = document.querySelector(".reveal");
    if (revealRoot) {
      revealRoot.appendChild(node);
    }

    return node;
  }

  function init() {
    if (!window.Reveal || typeof window.Reveal.getCurrentSlide !== "function") {
      return;
    }

    var indicator = ensureIndicatorNode();
    if (!indicator) {
      return;
    }

    var parentPathsBySlide = computeParentPaths();

    function renderPath() {
      var current = window.Reveal.getCurrentSlide();
      var path = parentPathsBySlide.get(current) || [];

      if (!path.length) {
        indicator.textContent = "";
        indicator.style.display = "none";
        return;
      }

      indicator.textContent = path.join(" > ");
      indicator.style.display = "block";
    }

    renderPath();
    window.Reveal.on("slidechanged", renderPath);
    window.Reveal.on("ready", function () {
      parentPathsBySlide = computeParentPaths();
      renderPath();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

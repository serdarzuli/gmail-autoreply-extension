console.log("Content script loaded.");

function getLastMailContent() {
    const mailElements = document.querySelectorAll("div[role='listitem']");
    const lastMail = mailElements[mailElements.length - 1];
    const mailText = lastMail?.innerText || "Mail içeriği bulunamadı";
    return mailText;
  }

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "getMailContent") {
      const emailBody = document.querySelector(".ii.gt")?.innerText || "No content mail";
      sendResponse({ content: emailBody });
      return true;
    }
  });
  
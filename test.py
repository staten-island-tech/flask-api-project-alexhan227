onsterCards.forEach(card => {
        const name = card.getAttribute("data-name");
        card.style.display = name.includes(query) ? "block" : "none";
      });
    });
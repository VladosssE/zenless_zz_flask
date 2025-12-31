document.addEventListener("DOMContentLoaded", () => {
	const forms = document.querySelectorAll(".main-character-card");

	forms.forEach(form => {
		form.addEventListener("submit", function (e) {
			e.preventDefault();

			const formData = new FormData(form);
			const data = {};

			formData.forEach((value, key) => {
				data[key] = value;
			});

			fetch(form.action, {
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
				body: JSON.stringify(data)
			})
			.then(res => res.json())
			.then(response => {
				if (response.status === "ok") {
					showSaveMessage(form, "Успешно сохранено");
				} else {
					showSaveMessage(form, "Ошибка сохранения", true);
				}
			})
			.catch(() => {
				showSaveMessage(form, "Ошибка ???", true);
			});
		});
	});
});

function showSaveMessage(form, text, isError = false) {
	const wrapper = form.querySelector(".save-button-wrapper");

	let message = wrapper.querySelector(".save-message");

	if (!message) {
		message = document.createElement("div");
		message.className = "save-message";
		wrapper.appendChild(message);
	}

	message.textContent = text;
	message.style.color = isError ? "red" : "green";

	requestAnimationFrame(() => {
		message.classList.add("visible");
	});

	setTimeout(() => {
		message.classList.remove("visible");
	}, 2000);
}

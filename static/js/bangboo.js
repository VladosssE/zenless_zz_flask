document.addEventListener("DOMContentLoaded", () => {
	const forms = document.querySelectorAll(".main-bangboo-card");

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
				showSaveMessage(form, "Ошибка соединения", true);
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
		wrapper.prepend(message);
	}

	message.textContent = text;
	message.classList.toggle('error', isError);
	message.style.opacity = "1";

	setTimeout(() => {
		message.style.opacity = "0";
	}, 2000);
}

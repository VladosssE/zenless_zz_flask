document.addEventListener("DOMContentLoaded", () => {
	const forms = document.querySelectorAll(".achievement-btn");

	forms.forEach(button => {
		const form = button.closest("form");

		form.addEventListener("submit", function(e) {
			e.preventDefault();

			const formData = new FormData(form);
			const godfingerId = formData.get("godfinger_id");

			fetch(form.action, {
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
				body: JSON.stringify({ godfinger_id: godfingerId })
			})
			.then(res => res.json())
			.then(data => {
				if (data.status === "Выполнено") {
					button.querySelector(".achievement").classList.add("ach-completed");
					button.querySelector(".status").classList.add("completed");
					button.querySelector(".status").classList.remove("not-completed");
				} else {
					button.querySelector(".achievement").classList.remove("ach-completed");
					button.querySelector(".status").classList.remove("completed");
					button.querySelector(".status").classList.add("not-completed");
				}
				button.querySelector(".status").textContent = data.status;
			})
			.catch(err => console.error("Ошибка обновления:", err));
		});
	});
});

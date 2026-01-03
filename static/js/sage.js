document.addEventListener("DOMContentLoaded", () => {
	const buttons = document.querySelectorAll(".achievement-btn");

	buttons.forEach(button => {
		const form = button.closest("form");
		if (!form) return;

		form.addEventListener("submit", (e) => {
			e.preventDefault();

			const formData = new FormData(form);
			const sageId = formData.get("sage_id");

			if (!sageId) {
				console.error("sage_id не найден");
				return;
			}

			fetch(form.action, {
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
				body: JSON.stringify({ sage_id: sageId })
			})
			.then(res => {
				if (!res.ok) throw new Error("Ошибка сервера");
				return res.json();
			})
			.then(data => {
				const achievement = button.querySelector(".achievement");
				const status = button.querySelector(".status");

				if (!achievement || !status) return;

				if (data.status === "Получено") {
					achievement.classList.add("ach-completed");
					status.classList.add("completed");
					status.classList.remove("not-completed");
				} else {
					achievement.classList.remove("ach-completed");
					status.classList.remove("completed");
					status.classList.add("not-completed");
				}

				status.textContent = data.status;
			})
			.catch(err => console.error("Ошибка обновления:", err));
		});
	});
});

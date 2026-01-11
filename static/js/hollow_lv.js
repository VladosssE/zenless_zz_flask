document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".column-content-btn");

    buttons.forEach(button => {
            const form = button.closest("form");
            if (!form) return;

            form.addEventListener("submit", (e) => {
                    e.preventDefault();

                    const formData = new FormData(form);
                    const hollow_lvId = formData.get("hollow_lv_id");

                    if (!hollow_lvId) {
                            console.error("hollow_lv_id не найден");
                            return;
                    }

                    fetch(form.action, {
                            method: "POST",
                            headers: {
                                    "Content-Type": "application/json"
                            },
                            body: JSON.stringify({ hollow_lv_id: hollow_lvId })
                    })
                    .then(res => {
                            if (!res.ok) throw new Error("Ошибка сервера");
                            return res.json();
                    })
                    .then(data => {
                            const achievement = button.querySelector(".column-content");
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

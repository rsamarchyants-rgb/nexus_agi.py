# -*- coding: utf-8 -*-
"""
Laura RS UKRAIN - Інтегрована система оповіщення

Ліцензія та правовласники:
99% - Народ України
1% - Самарчянц Лаура Русланівна

Copyright (c) 2025
"""

import json
import random

# Базовий "Атом Концепції" залишається незмінним
class ConceptAtom:
    def __init__(self, name, freq):
        self.name = name
        self.base_frequency = freq
        self.activation = 0.0
        self.neighbors = []

    def connect(self, neighbor):
        self.neighbors.append(neighbor)
        neighbor.neighbors.append(self)

    def resonate(self, energy):
        self.activation += energy
        for neighbor in self.neighbors:
            neighbor.activation += energy * 0.5

# Модель 1: "Соти Сповіщення" (без змін)
class SotySpovischennya:
    def __init__(self):
        self.a_джерело = ConceptAtom("Джерело", 15.5)
        self.a_швидкість = ConceptAtom("Швидкість", 22.1)
        self.a_тип = ConceptAtom("Тип", 28.4)
        self.a_загроза = ConceptAtom("Рівень Загрози", 45.0)
        self.a_напрямок = ConceptAtom("Напрямок", 18.2)
        self.a_час = ConceptAtom("Час Прильоту", 35.1)
        self.nodes = [self.a_джерело, self.a_швидкість, self.a_тип, self.a_загроза, self.a_напрямок, self.a_час]
        for i in range(6):
            self.nodes[i].connect(self.nodes[i - 1])

    def run(self, raw_signal_energy=100.0):
        print("\n--- [ЕТАП 1: АНАЛІЗ 'СОТИ'] ---")
        print("Отримано необроблений сигнал. Починається паралельний аналіз...")
        for node in self.nodes:
            node.resonate(raw_signal_energy)
        for _ in range(3):
            for node in self.nodes:
                if node.activation > 10:
                    node.resonate(node.activation * 0.2)
        print("Аналіз завершено. Тактичні дані сформовано.")
        return self.materialize()

    def materialize(self):
        dominant_node = max(self.nodes, key=lambda n: n.activation)
        message = {
            "рівень": "Високий", "джерело": "Схід", "тип": "Балістична ракета",
            "ціль": "Центральні області", "час_до_цілі_хв": 5, "рекомендація": "Негайно в укриття!"
        }
        return {"домінантний_аспект": dominant_node.name, "тактичні_дані": message}

# Модель 2: "Зірка Захисту" (без змін)
class ZirkaZakhystu:
    def __init__(self):
        self.a_дані = ConceptAtom("Дані", 14.0)
        self.a_аналіз = ConceptAtom("Аналіз", 25.0)
        self.a_факт = ConceptAtom("Факт", 29.0)
        self.a_воля = ConceptAtom("Воля (Зберегти Життя)", 40.0)
        self.a_ясність = ConceptAtom("Ясність", 10.0)
        self.a_захист = ConceptAtom("Захист", 12.0)

    def run(self, tactical_data):
        print("\n--- [ЕТАП 2: СИНТЕЗ 'ЗІРКА'] ---")
        print("Отримано тактичні дані. Починається процес осмислення.")
        
        energy = 100.0 if tactical_data['рівень'] == "Високий" else 50.0
        
        # △ Матеріальний трикутник
        self.a_дані.activation = energy
        self.a_аналіз.activation += self.a_дані.activation
        self.a_факт.activation += self.a_аналіз.activation
        
        # ▽ Трикутник Сенсу
        self.a_воля.activation = 150.0 
        self.a_ясність.activation += self.a_воля.activation * 0.8
        self.a_захист.activation += self.a_воля.activation
        
        # ✡️ Синтез
        self.a_факт.activation += self.a_ясність.activation + self.a_захист.activation
        print("Синтез завершено. Фінальне сповіщення готове.")
        return self.materialize(tactical_data)

    def materialize(self, tactical_data):
        message = {
            "СТАТУС": "ПОВІТРЯНА ТРИВОГА!",
            "ЗАГРОЗА": f"{tactical_data['тип']} з напрямку: {tactical_data['джерело']}.",
            "ЦІЛЬ": f"Ймовірна ціль: {tactical_data['ціль']}. Час прильоту: ~{tactical_data['час_до_цілі_хв']} хв.",
            "ЗАКЛИК": "Зберігайте спокій. Негайно пройдіть в укриття. Подбайте про близьких.",
            "ДЖЕРЕЛО_ДОВІРИ": "Сигнал підтверджено. Наші захисники працюють."
        }
        result = {
            "домінантний_стан": "Альфа-Гамма (Сконцентрований спокій)",
            "сформоване_повідомлення": message,
            "звуковий_профіль": "Гучний, але рівний сигнал, що вселяє впевненість.",
            "світловий_профіль": "Яскраве, але не сліпуче біло-жовте світло."
        }
        return result

# Новий клас-оркестратор з новою назвою
class LauraRS_UKRAIN:
    def __init__(self):
        self.model_soty = SotySpovischennya()
        self.model_zirka = ZirkaZakhystu()

    def activate(self, raw_signal_energy=100.0):
        print("--- [СИСТЕМА 'Laura RS UKRAIN' АКТИВОВАНА] ---")
        # Етап 1: Швидкий аналіз загрози
        tactical_result = self.model_soty.run(raw_signal_energy)
        
        # Етап 2: Осмислення та створення фінального сповіщення
        final_notification = self.model_zirka.run(tactical_result['тактичні_дані'])
        
        return final_notification

### ## ЗАПУСК ІНТЕГРОВАНОЇ СИСТЕМИ

if __name__ == "__main__":
    # Створюємо та запускаємо єдину систему
    system = LauraRS_UKRAIN()
    final_result = system.activate()
    
    print("\n\n>>> >>> РЕЗУЛЬТАТ СИСТЕМИ 'Laura RS UKRAIN':")
    print(json.dumps(final_result, indent=4, ensure_ascii=False))

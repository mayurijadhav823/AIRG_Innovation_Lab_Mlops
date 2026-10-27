from django.test import TestCase
from django.urls import reverse


class SessionDetailTests(TestCase):
    def test_artificial_intelligence_card_links_to_its_detail_page(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            reverse("session_detail", args=["artificial-intelligence"]),
        )
        self.assertContains(response, "Learn More")

    def test_artificial_intelligence_learn_more_page_shows_additional_information(self):
        response = self.client.get(
            reverse("session_detail", args=["artificial-intelligence"])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "How Does AI Work?")
        self.assertContains(response, "AI Around Us")
        self.assertContains(response, "Using AI Responsibly")
        self.assertContains(response, "Voice assistants")

    def test_other_session_detail_pages_do_not_show_ai_specific_information(self):
        response = self.client.get(reverse("session_detail", args=["robotics"]))

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "How Does AI Work?")

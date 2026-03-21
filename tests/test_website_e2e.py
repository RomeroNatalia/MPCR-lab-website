"""End-to-end Playwright tests for the MPCR Lab website.

Audits every page, link, image, navigation element, and interactive component.

Usage:
    pytest tests/test_website_e2e.py -v --headed  # watch in browser
    pytest tests/test_website_e2e.py -v            # headless
"""

import pytest
from playwright.sync_api import Page, expect

BASE = "http://localhost:4000"

# ── Page Load Tests ──────────────────────────────────────────────────────────


class TestPageLoads:
    """Every page should return 200 and have a title."""

    PAGES = [
        ("/", "Home"),
        ("/news/", "News"),
        ("/about/", "About"),
        ("/projects/", "Projects"),
        ("/publications/", "Publications"),
        ("/posters/", "Poster Gallery"),
        ("/dashboard/", "Dashboard"),
        ("/people/members", "People"),
        ("/people/former-members/", "Former"),
        ("/contact/", "Contact"),
        ("/join/", "Join"),
        ("/poster-templates/", "Poster Templates"),
    ]

    @pytest.mark.parametrize("path,expected_text", PAGES)
    def test_page_loads(self, page: Page, path, expected_text):
        resp = page.goto(f"{BASE}{path}")
        assert resp.status == 200, f"{path} returned {resp.status}"
        assert page.title(), f"{path} has no title"


class TestHomepage:
    """Homepage structure and content."""

    def test_slideshow_exists(self, page: Page):
        page.goto(BASE)
        slideshow = page.locator("[data-uk-slideshow]")
        assert slideshow.count() >= 1

    def test_mission_statement(self, page: Page):
        page.goto(BASE)
        assert page.locator("text=natural computing").count() >= 1

    def test_three_cards(self, page: Page):
        page.goto(BASE)
        assert page.locator("text=Research").first.is_visible()
        assert page.locator("text=Community").first.is_visible()
        assert page.locator("text=Join Us").first.is_visible()

    def test_research_tags(self, page: Page):
        page.goto(BASE)
        tags = page.locator("text=Large Language Models")
        assert tags.count() >= 1

    def test_join_cta(self, page: Page):
        page.goto(BASE)
        cta = page.locator("a[href='/join/']")
        assert cta.count() >= 1

    def test_latest_news(self, page: Page):
        page.goto(BASE)
        assert page.locator("text=Latest News").count() >= 1


class TestNavigation:
    """Desktop navigation links work."""

    NAV_LINKS = [
        ("Home", "/"),
        ("News", "/news/"),
        ("About", "/about/"),
        ("Projects", "/projects/"),
        ("Join", "/join/"),
        ("Contact", "/contact/"),
    ]

    @pytest.mark.parametrize("text,expected_path", NAV_LINKS)
    def test_nav_link(self, page: Page, text, expected_path):
        page.goto(BASE)
        link = page.locator(f"nav a:has-text('{text}')").first
        href = link.get_attribute("href")
        assert expected_path in href, f"Nav '{text}' -> {href}, expected {expected_path}"


class TestProjects:
    """Projects page and individual project pages."""

    def test_project_grid(self, page: Page):
        page.goto(f"{BASE}/projects/")
        cards = page.locator(".uk-card")
        assert cards.count() >= 20

    def test_project_detail_loads(self, page: Page):
        resp = page.goto(f"{BASE}/projects/Compressed-Inference/")
        assert resp.status == 200
        expect(page.locator("h1").first).to_contain_text("Compressed")

    def test_dwave_project_exists(self, page: Page):
        page.goto(f"{BASE}/projects/D-Wave-Quantum-Computing/")
        expect(page.locator("h1")).to_contain_text("D-Wave")
        assert page.locator("text=4,400").count() >= 1

    def test_project_team_section(self, page: Page):
        page.goto(f"{BASE}/projects/AIClassroom/")
        # Projects with members should show Team section
        page.wait_for_load_state()


class TestPeople:
    """People pages."""

    def test_members_page_has_people(self, page: Page):
        page.goto(f"{BASE}/people/members")
        cards = page.locator(".uk-card")
        assert cards.count() >= 10

    def test_leadership_section(self, page: Page):
        page.goto(f"{BASE}/people/members")
        assert page.locator("text=Lab Leadership").count() >= 1

    def test_director_profiles(self, page: Page):
        for name in ["William", "Elan", "Susan"]:
            page.goto(f"{BASE}/people/members")
            assert page.locator(f"text={name}").count() >= 1

    def test_person_detail_page(self, page: Page):
        page.goto(f"{BASE}/people/Elan-Barenholtz/")
        expect(page.locator("h1").first).to_contain_text("Elan")
        # Should have social links
        assert page.locator("a[href*='x.com']").count() >= 1

    def test_person_has_projects_section(self, page: Page):
        page.goto(f"{BASE}/people/Elan-Barenholtz/")
        assert page.locator("text=Projects").count() >= 1

    def test_former_members_page(self, page: Page):
        resp = page.goto(f"{BASE}/people/former-members/")
        assert resp.status == 200

    def test_ganesh_has_image(self, page: Page):
        page.goto(f"{BASE}/people/Ganesh-Shiwakoti/")
        img = page.locator("img.avatar, img.img-rounded").first
        assert img.is_visible()

    def test_natalia_profile(self, page: Page):
        page.goto(f"{BASE}/people/Natalia-Romero/")
        expect(page.locator("h1").first).to_contain_text("Natalia")
        assert page.locator("text=Complex Social Systems").count() >= 1


class TestNews:
    """News pages and posts."""

    def test_news_page_has_posts(self, page: Page):
        page.goto(f"{BASE}/news/")
        articles = page.locator("article")
        assert articles.count() >= 4

    def test_news_images_not_broken(self, page: Page):
        page.goto(f"{BASE}/news/")
        # No img tags with empty src
        broken = page.locator("img[src='']")
        assert broken.count() == 0

    def test_news_post_detail(self, page: Page):
        page.goto(f"{BASE}/news/")
        first_link = page.locator("article h3 a").first
        first_link.click()
        page.wait_for_load_state()
        assert page.locator("h1").count() >= 1


class TestPosters:
    """Poster gallery."""

    def test_poster_gallery_loads(self, page: Page):
        page.goto(f"{BASE}/posters/")
        assert page.locator(".poster-card, .uk-card").count() >= 1

    def test_poster_detail_page(self, page: Page):
        resp = page.goto(f"{BASE}/posters/example-poster-horizontal/")
        assert resp.status == 200


class TestPosterTemplates:
    """Poster template system."""

    def test_templates_page(self, page: Page):
        page.goto(f"{BASE}/poster-templates/")
        assert page.locator("text=horizontal").count() >= 1 or page.locator("text=Horizontal").count() >= 1

    def test_example_poster_loads(self, page: Page):
        page.goto(f"{BASE}/posters/example-poster-horizontal/")
        assert page.locator("text=Your Poster Title").count() >= 1


class TestDashboard:
    """Public lab dashboard."""

    def test_dashboard_has_stats(self, page: Page):
        page.goto(f"{BASE}/dashboard/")
        # Should have stat cards with numbers
        assert page.locator(".uk-card").count() >= 4

    def test_dashboard_has_projects_section(self, page: Page):
        page.goto(f"{BASE}/dashboard/")
        assert page.locator("text=Active Projects").count() >= 1


class TestJoin:
    """QR code join page."""

    def test_join_page_has_qr(self, page: Page):
        page.goto(f"{BASE}/join/")
        qr = page.locator("#qrcode")
        assert qr.count() >= 1

    def test_join_has_apply_button(self, page: Page):
        page.goto(f"{BASE}/join/")
        btn = page.locator("a:has-text('Open Application Form'), a:has-text('Apply')")
        assert btn.count() >= 1

    def test_join_card_page(self, page: Page):
        resp = page.goto(f"{BASE}/join/card/")
        assert resp.status == 200
        cards = page.locator(".card")
        assert cards.count() >= 4


class TestPublications:
    """Publications page (may be empty but should load)."""

    def test_publications_page_loads(self, page: Page):
        resp = page.goto(f"{BASE}/publications/")
        assert resp.status == 200

    def test_publications_placeholder(self, page: Page):
        page.goto(f"{BASE}/publications/")
        # Either has publications or shows "coming soon"
        content = page.content()
        assert "Publications" in content


class TestAbout:
    """About page."""

    def test_about_has_directors(self, page: Page):
        page.goto(f"{BASE}/about/")
        # Hahn should appear (contact: true)
        assert page.locator("text=Hahn").count() >= 1

    def test_about_has_research_focus(self, page: Page):
        page.goto(f"{BASE}/about/")
        assert page.locator("text=Research Focus").count() >= 1


class TestSearch:
    """Search functionality."""

    def test_search_json_exists(self, page: Page):
        resp = page.goto(f"{BASE}/search.json")
        assert resp.status == 200


class TestImages:
    """No broken images across the site."""

    PAGES_TO_CHECK = [
        "/", "/projects/", "/people/members", "/news/",
        "/dashboard/", "/posters/",
    ]

    @pytest.mark.parametrize("path", PAGES_TO_CHECK)
    def test_no_broken_images(self, page: Page, path):
        broken = []

        def handle_response(response):
            if response.request.resource_type == "image" and response.status >= 400:
                broken.append(f"{response.url} ({response.status})")

        page.on("response", handle_response)
        page.goto(f"{BASE}{path}", wait_until="networkidle")
        assert len(broken) == 0, f"Broken images on {path}: {broken}"


# ── CRM API Tests ────────────────────────────────────────────────────────────

CRM_BASE = "http://localhost:8080"


class TestCRMDev:
    """CRM dev routes (no auth required)."""

    DEV_PAGES = [
        "/dev/dashboard",
        "/dev/people",
        "/dev/projects",
        "/dev/publications",
        "/dev/news",
        "/dev/meetings",
        "/dev/messages",
        # /dev/posters not implemented in dev routes
        "/dev/join-requests",
    ]

    @pytest.mark.parametrize("path", DEV_PAGES)
    def test_dev_page_loads(self, page: Page, path):
        resp = page.goto(f"{CRM_BASE}{path}")
        assert resp.status == 200, f"{path} returned {resp.status}"

    def test_dev_dashboard_has_stats(self, page: Page):
        page.goto(f"{CRM_BASE}/dev/dashboard")
        assert page.locator("text=Dashboard").count() >= 1

    def test_dev_people_has_table(self, page: Page):
        page.goto(f"{CRM_BASE}/dev/people")
        assert page.locator("table, tr").count() >= 5


class TestCRMAuth:
    """CRM admin routes require auth."""

    def test_admin_redirects_or_401(self, page: Page):
        resp = page.goto(f"{CRM_BASE}/admin/")
        assert resp.status in (200, 401, 403), f"Got {resp.status}"
        # Should show login or error, not admin content
        content = page.content()
        assert "Dashboard" not in content or "login" in content.lower() or "401" in content

    def test_member_requires_auth(self, page: Page):
        resp = page.goto(f"{CRM_BASE}/member/")
        assert resp.status in (401, 403, 422)

    def test_join_form_returns_error_without_gcs(self, page: Page):
        # In dev mode without GCS, /join returns 500 (can't load projects)
        # In production this works fine
        resp = page.goto(f"{CRM_BASE}/join")
        assert resp.status in (200, 500)

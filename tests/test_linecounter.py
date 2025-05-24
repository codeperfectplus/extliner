import unittest
import tempfile
from pathlib import Path
from extliner.main import LineCounter


class TestLineCounter(unittest.TestCase):

    # inbuilt setup and teardown methods to create a temporary directory for testing
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.base_path = Path(self.temp_dir.name)

    # it will call the cleanup method of TemporaryDirectory to delete the directory after tests
    def tearDown(self):
        self.temp_dir.cleanup()

    def create_file(self, relative_path: str, content: str):
        file_path = self.base_path / relative_path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")

    def test_single_file_with_and_without_spaces(self):
        self.create_file("hello.py", "print('Hello')\n\nprint('World')\n")

        counter = LineCounter()
        result = counter.count_lines(self.base_path)

        self.assertIn(".py", result)
        self.assertEqual(result[".py"]["with_spaces"], 3)
        self.assertEqual(result[".py"]["without_spaces"], 2)

    def test_multiple_extensions(self):
        self.create_file("a.py", "print('a')\n\n")
        self.create_file("b.js", "console.log('b');\n")
        self.create_file("c.txt", "\n\ntext\n\n")

        counter = LineCounter()
        result = counter.count_lines(self.base_path)

        self.assertEqual(result[".py"]["with_spaces"], 2)
        self.assertEqual(result[".py"]["without_spaces"], 1)
        self.assertEqual(result[".js"]["with_spaces"], 1)
        self.assertEqual(result[".js"]["without_spaces"], 1)
        self.assertEqual(result[".txt"]["with_spaces"], 4)
        self.assertEqual(result[".txt"]["without_spaces"], 1)

    def test_ignore_extensions(self):
        self.create_file("a.py", "code\ncode\n")
        self.create_file("b.txt", "text\ntext\n")

        counter = LineCounter(ignore_extensions=[".txt"])
        result = counter.count_lines(self.base_path)

        self.assertIn(".py", result)
        self.assertNotIn(".txt", result)

    def test_no_extension_file(self):
        self.create_file("README", "line1\nline2\n")

        counter = LineCounter()
        result = counter.count_lines(self.base_path)

        self.assertIn("NO_EXT", result)
        self.assertEqual(result["NO_EXT"]["with_spaces"], 2)
        self.assertEqual(result["NO_EXT"]["without_spaces"], 2)

    def test_to_json_format(self):
        self.create_file("sample.py", "x = 1\n\ny = 2\n")

        counter = LineCounter()
        data = counter.count_lines(self.base_path)
        json_str = counter.to_json(data)

        self.assertTrue(json_str.startswith("{"))
        self.assertIn('"with_spaces":', json_str)
        self.assertIn('"without_spaces":', json_str)


if __name__ == "__main__":
    unittest.main()

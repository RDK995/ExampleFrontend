const fs = require('fs');
const path = require('path');

const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');

describe('index.html', () => {
  describe('header', () => {
    test('contains the app heading', () => {
      expect(html).toContain('Hello React');
    });
  });

  describe('content section', () => {
    test('has a content section element with id "content"', () => {
      expect(html).toContain("id: 'content'");
    });

    test('has a Welcome heading', () => {
      expect(html).toContain('Welcome');
    });

    test('has sample content text', () => {
      expect(html).toContain('sample content section');
    });

    test('has the shell script description', () => {
      expect(html).toContain('runs locally with a shell script');
    });
  });
});

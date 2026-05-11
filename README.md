# Vault - Self-Hostable URL Bookmark Manager

A modern, self-hostable bookmark manager built with Flask and SQLAlchemy. Store, organize, and access your favorite URLs with a beautiful interface featuring favicons, search, drag-and-drop reordering, and dark mode support.

## Features

- 🔗 **URL Bookmarks**: Store and manage your favorite websites with custom names
- 🖼️ **Favicon Display**: Automatic favicon fetching and display for each bookmark
- 🔍 **Search Functionality**: Quick search through bookmark names and URLs
- 🖱️ **Drag & Drop**: Reorder bookmarks with intuitive drag handles
- 🌙 **Dark Mode**: Toggle between light and dark themes
- 📋 **Copy to Clipboard**: One-click URL copying with visual feedback
- ✏️ **Edit Bookmarks**: Modify bookmark names and URLs
- 🗑️ **Delete Bookmarks**: Remove unwanted bookmarks with confirmation
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices
- 🚀 **Self-Hostable**: Run on your own server with minimal setup

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Setup

1. **Clone or download the project files**

2. **Navigate to the Url_Store directory**
   ```bash
   cd Url_Store
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser** and visit `http://localhost:5000`

## Usage

### Adding Bookmarks
- Click the "+" button in the header
- Enter a display name for the bookmark
- Enter the full URL (including https://)
- Click "Save to Vault"

### Managing Bookmarks
- **Search**: Use the search bar to filter bookmarks by name or URL
- **Reorder**: Drag bookmarks using the grip handle (⋮⋮) to rearrange them
- **Copy URL**: Click the copy icon to copy the URL to clipboard
- **Edit**: Click the edit icon to modify bookmark details
- **Delete**: Click the trash icon to remove a bookmark (with confirmation)
- **Open**: Click on any URL to open it in a new tab

### Features
- **Favicon Display**: Automatic favicon loading from each website
- **Dark Mode**: Toggle with the moon/sun icon in the header
- **Responsive**: Adapts to different screen sizes
- **Visual Feedback**: Copy confirmation and hover effects

## Project Structure

```
Url_Store/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── instance/           # SQLite database storage
└── templates/
    └── index.html      # Main UI template
```

## Dependencies

- Flask==3.1.3
- Flask-SQLAlchemy==3.1.1
- SQLAlchemy==2.0.49

## Database

The application uses SQLite (`bookmarks.db`) which is automatically created when you first run the app. The database includes:
- Bookmark name (display title)
- URL (full web address)
- Auto-incrementing ID

## Favicon Integration

The application automatically fetches favicons using Google's favicon service:
```
https://www.google.com/s2/favicons?sz=64&domain={domain}
```

This provides consistent 64x64 pixel favicons for all bookmarked sites.

## Customization

### Styling
The UI uses Tailwind CSS and can be customized by modifying the `<style>` section in `templates/index.html`.

### Features
- **Persistent Ordering**: Currently drag-and-drop reordering is visual only. To persist order, implement a position field in the database and update the reorder endpoint.
- **Categories/Tags**: Add categorization by extending the Bookmark model with a category field.
- **Import/Export**: Add functionality to import bookmarks from browser exports or export to HTML.

### Database
For production use, consider switching to PostgreSQL or MySQL by updating the `SQLALCHEMY_DATABASE_URI` in `app.py`.

## Security Notes

- This is a basic implementation for personal use
- For production deployment, consider:
  - Using environment variables for configuration
  - Adding user authentication
  - Implementing URL validation
  - Adding rate limiting for favicon requests
  - Setting up proper database backups

## Browser Compatibility

- Modern browsers with ES6+ support
- Clipboard API support for copy functionality
- CSS Grid and Flexbox support

## License

MIT License - feel free to use and modify for your own projects.

## Contributing

Feel free to submit issues and enhancement requests!</content>

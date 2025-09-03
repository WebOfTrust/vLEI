mermaid.initialize({
  startOnLoad: true,
  theme: 'default',
  flowchart: {
    useMaxWidth: true,
    htmlLabels: true,
    curve: 'linear'
  },
  elk: {
    'elk.algorithm': 'layered',
    'elk.direction': 'DOWN',
    'elk.layered.spacing.nodeNodeBetweenLayers': 50,
    'elk.layered.spacing.edgeNodeBetweenLayers': 20,
    'elk.edge.routing': 'ORTHOGONAL', 
    'elk.layered.edgeRouting.selfLoopDistribution': 'EQUALLY',
    'elk.layered.nodePlacement.strategy': 'BRANDES_KOEPF',
    'elk.layered.crossingMinimization.strategy': 'LAYER_SWEEP'
  }
});

const contentFiles = {};

const knownFiles = [
  'index', 'credentials', 'vlei-credential-ecosystem', 'vlei-dependency-graph',
  'qvi-credential-schema', 'legal-entity-credential-schema', 'ecr-credential-schema',
  'oor-credential-schema', 'ecr-auth-credential-schema', 'oor-auth-credential-schema'
];

async function loadcontentFiles() {
  console.log('Loading content files...');
  let loadedCount = 0;
  
  for (const file of knownFiles) {
    try {
      const response = await fetch(`content/${file}.md`);
      if (response.ok) {
        contentFiles[file] = await response.text();
        loadedCount++;
        console.log(`✓ Loaded ${file}.md`);
      } else {
        console.log(`✗ Failed to load ${file}.md (${response.status})`);
      }
    } catch (error) {
      console.log(`✗ Error loading ${file}.md:`, error);
    }
  }
  
  console.log(`Loaded ${loadedCount} of ${knownFiles.length} content files`);
}

async function loadPage(pageName) {
  const content = document.getElementById('content-content');
  
  if (!contentFiles[pageName]) {
    content.innerHTML = `
      <div class="loading">
        <h2>Page Not Found</h2>
        <p>The requested page "${pageName}" could not be loaded.</p>
      </div>
    `;
    return;
  }

  content.innerHTML = '<div class="loading">Loading...</div>';

  try {
  
    let html = marked.parse(contentFiles[pageName]);
    html = html.replace(
      /<pre><code class="language-mermaid">([\s\S]*?)<\/code><\/pre>/g,
      '<div class="mermaid">$1</div>'
    );
    
    content.innerHTML = html;
    
    const links = content.querySelectorAll('a[href]:not([href^="http"]):not([href^="#"])');
    links.forEach(link => {
      const href = link.getAttribute('href');
      const pageName = href.replace(/^\//, '').replace(/\/$/, '');
      
      if (contentFiles[pageName]) {
        link.onclick = (e) => {
          e.preventDefault();
          loadPage(pageName);
          return false;
        };
      }
    });
    
    const mermaidElements = content.querySelectorAll('.mermaid');
    if (mermaidElements.length > 0) {
      mermaid.init(undefined, mermaidElements);
      
      mermaidElements.forEach(diagram => {
        diagram.addEventListener('click', function(e) {
          if (this.classList.contains('zoomed')) {
            const rect = this.getBoundingClientRect();
            const isCloseButton = e.clientX > rect.right - 50 && e.clientY < rect.top + 50;
            
            if (isCloseButton) {
              this.classList.remove('zoomed');
              document.body.style.overflow = '';
              return;
            }
            
            if (e.target.closest('svg')) return;
            
            this.classList.remove('zoomed');
            document.body.style.overflow = '';
          } else {
            if (e.target.tagName === 'A') return;
            
            this.classList.add('zoomed');
            document.body.style.overflow = 'hidden';
          }
        });
      });
    }
    
    window.scrollTo({ top: 0, behavior: 'smooth' });
    
  } catch (error) {
    content.innerHTML = `
      <div class="loading">
        <h2>Error</h2>
        <p>Could not render the page: ${error.message}</p>
      </div>
    `;
  }
}

async function init() {
  document.getElementById('content-content').innerHTML = `
    <div class="loading">
      <h2>Loading Documentation...</h2>
      <p>Please wait while we load the vLEI documentation files.</p>
    </div>
  `;
  
  await loadcontentFiles();
  
  const loadedFiles = Object.keys(contentFiles);
  if (loadedFiles.length > 0) {
    const startPage = contentFiles['index'] ? 'index' : loadedFiles[0];
    loadPage(startPage);
  } else {
    document.getElementById('content-content').innerHTML = `
      <div class="loading">
        <h2>Unable to Load Documentation</h2>
        <p>No content files could be loaded. Please check that the content files are available in the <code>content/</code> directory.</p>
        <p><strong>Expected files:</strong> ${knownFiles.join(', ')}</p>
      </div>
    `;
  }
}

// Keyboard support for zoomed diagrams
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    const zoomedDiagram = document.querySelector('.mermaid.zoomed');
    if (zoomedDiagram) {
      zoomedDiagram.classList.remove('zoomed');
      document.body.style.overflow = '';
    }
  }
});

document.addEventListener('DOMContentLoaded', init);

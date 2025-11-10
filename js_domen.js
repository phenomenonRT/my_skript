const domains = new Set();

function getDomain(url) {
  try {
    const { hostname } = new URL(url);
    return hostname;
  } catch (e) {
    return null;
  }
}

const resources = performance.getEntriesByType('resource');

resources.forEach((resource) => {
  const domain = getDomain(resource.name);
  if (domain) {
    domains.add(domain);
  }
});

const sortedDomains = Array.from(domains).sort();
sortedDomains.forEach((domain) => console.log(domain));
=-------------------------------------------------------------------------------------------------
function listDomains() {
  const domains = new Set();

  function getDomain(url) {
    try {
      return new URL(url).hostname;
    } catch {
      return null;
    }
  }

  const resources = performance.getEntriesByType('resource');

  for (const resource of resources) {
    const domain = getDomain(resource.name);
    if (domain) domains.add(domain);
  }

  const sortedDomains = Array.from(domains).sort();

  for (const domain of sortedDomains) {
    console.log(domain);
  }
}

// вызов
listDomains();

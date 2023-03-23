# App-level API keys
type ManifestServiceHttpAuth  = BaseManifestAuth & {
  type: 'service_http',
  authorization_type: HttpAuthorizationType
  verification_tokens: {
    [service: string]?: string
  }
}

# User-level HTTP authentication
type ManifestUserHttpAuth  = BaseManifestAuth & {
  type: 'user_http'
  authorization_type: HttpAuthorizationType
}

type ManifestOAuthAuth  = BaseManifestAuth & {
  type: 'oauth',

  # OAuth URL where a user is directed to for the OAuth authentication flow to begin.
  client_url: string

  # OAuth scopes required to accomplish operations on the user's behalf.
  scope: string

  # Endpoint used to exchange OAuth code with access token.
  authorization_url: string

  # When exchanging OAuth code with access token, the expected header 'content-type'. For example: 'content-type: application/json'
  authorization_content_type: string;

  # When registering the OAuth client ID and secrets, the plugin service will surface a unique token. 
  verification_tokens: {
    [service: string]?: string
  }
}

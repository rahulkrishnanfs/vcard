import { Container } from 'react-bootstrap'
import Reveal from './Reveal'
import { cursorNorthampton as cn } from '../data'

export default function CursorNorthampton() {
  return (
    <section id="cursor-northampton" className="section community-banner-section">
      <Container>
        <Reveal className="community-banner">
          <span className="community-banner-glow" aria-hidden="true"></span>
          <div className="community-banner-inner">
            <div className="community-banner-main">
              <span className="live-badge">
                <span className="live-dot" aria-hidden="true"></span>
                {cn.badge}
              </span>
              <h2 className="community-banner-title">
                Building <span className="gradient-text">{cn.name}</span>
              </h2>
              <p className="community-banner-lead">{cn.tagline}</p>
              <p className="community-banner-text">{cn.text}</p>
              <div className="community-banner-actions">
                <a
                  href={cn.link}
                  target="_blank"
                  rel="noreferrer"
                  className="btn btn-glow"
                >
                  <i className="bi bi-people-fill me-2"></i>
                  {cn.linkLabel}
                  <i className="bi bi-arrow-up-right ms-2"></i>
                </a>
              </div>
            </div>
            <div className="community-banner-stats">
              {cn.highlights.map((h) => (
                <div className="community-banner-stat" key={h.label}>
                  <span className="community-banner-num">{h.num}</span>
                  <span className="community-banner-stat-label">{h.label}</span>
                </div>
              ))}
            </div>
          </div>
        </Reveal>
      </Container>
    </section>
  )
}

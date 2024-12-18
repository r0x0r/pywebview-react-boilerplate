import styles from './Header.module.css'
import logo from '../../assets/logo.png'


export default function Header() {
  return (
    <div className={styles.headerContainer}>
      <img className={styles.logo} src={logo} alt='pywebview'/>
      <h2 className={styles.title}>pywebview</h2>

      <div className={styles.links}>
        <a className={styles.link} href='https://pywebview.flowrl.com/' target='_blank'>Documentation</a>
      </div>
    </div>
  );
};

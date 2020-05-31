export class LRUChache {
  private readonly capacity: number;
  private cache = new Map();

  constructor(capacity: number) {
    this.capacity = capacity;
  }

  public get(key: number): number {
    if (!this.cache.has(key)) {
      return -1;
    }

    const val = this.cache.get(key);
    this.cache.set(key, val);
    return val;
  }

  public put(key: number, val: number): void {
    if (this.cache.has(key)) {
      this.cache.delete(key);
    }
    if (this.cache.size >= this.capacity) {
      this.cache.delete(this.cache.keys().next().value);
    }
    this.cache.set(key, val);
  }
}
